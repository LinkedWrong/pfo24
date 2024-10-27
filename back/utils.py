import pandas as pd

from io import BytesIO

import pandas as pd
import sklearn.utils

from datetime import datetime

def make_dataframe(bytearray: bytes) -> pd.DataFrame:
    return pd.read_csv(BytesIO(bytearray), sep=';', encoding='windows-1251', low_memory=False)

def make_dataframe_from_path(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep=";", encoding='windows-1251', low_memory=False)

def make_input(cntrbtrs_clnts_ops: pd.DataFrame, trnsctns_ops: pd.DataFrame) -> pd.DataFrame:
    # Обработка пропусков: добавим индикаторы для некоторых столбцов и заменим NaN на 0 или "Unknown"
    for col in ['brth_plc', 'email', 'phn']:
        cntrbtrs_clnts_ops[col + '_missing'] = cntrbtrs_clnts_ops[col].isna().astype(int)  # индикатор пропуска
        if cntrbtrs_clnts_ops[col].dtype == 'object':
            cntrbtrs_clnts_ops[col].fillna('Unknown', inplace=True)
        else:
            cntrbtrs_clnts_ops[col].fillna(0, inplace=True)


    # Рассчитаем текущий год
    current_year = datetime.now().year
    # 1. Возраст клиента при заключении договора

    cntrbtrs_clnts_ops['accnt_bgn_date'] = pd.to_datetime(cntrbtrs_clnts_ops['accnt_bgn_date'], errors='coerce')
    cntrbtrs_clnts_ops['age_at_contract'] = cntrbtrs_clnts_ops['prsnt_age'] - (
        (current_year - cntrbtrs_clnts_ops['accnt_bgn_date'].dt.year).fillna(0))

    cntrbtrs_clnts_ops['age_vs_pension'] = cntrbtrs_clnts_ops['age_at_contract'] - cntrbtrs_clnts_ops['pnsn_age']

    def aggregate_transactions(df, period='3M'):
        df['oprtn_date'] = pd.to_datetime(df['oprtn_date'], errors='coerce')
        recent_transactions = df[df['oprtn_date'] > (datetime.now() - pd.DateOffset(months=int(period[:-1])))]
        avg_sum = recent_transactions.groupby('accnt_id')['sum'].mean().fillna(0).rename(f'avg_sum_{period}')
        std_sum = recent_transactions.groupby('accnt_id')['sum'].std().fillna(0).rename(f'std_sum_{period}')
        freq = recent_transactions.groupby('accnt_id').size().rename(f'transaction_freq_{period}')
        return avg_sum, std_sum, freq

    avg_sum_3m, std_sum_3m, freq_3m = aggregate_transactions(trnsctns_ops, '3M')
    avg_sum_6m, std_sum_6m, freq_6m = aggregate_transactions(trnsctns_ops, '6M')

    transaction_features = pd.DataFrame({
        'avg_sum_3M': avg_sum_3m,
        'std_sum_3M': std_sum_3m,
        'transaction_freq_3M': freq_3m,
        'avg_sum_6M': avg_sum_6m,
        'std_sum_6M': std_sum_6m,
        'transaction_freq_6M': freq_6m
    })

    def calculate_movement_type_ratios(df):
        movement_counts = df.groupby(['accnt_id', 'mvmnt_type']).size().unstack(fill_value=0)
        movement_ratios = movement_counts.div(movement_counts.sum(axis=1), axis=0)
        movement_ratios = movement_ratios.add_prefix('mvmnt_type_ratio_')
        return movement_ratios

    movement_type_ratios = calculate_movement_type_ratios(trnsctns_ops)
    cntrbtrs_clnts_ops = cntrbtrs_clnts_ops.merge(movement_type_ratios, on='accnt_id', how='left')
    cntrbtrs_clnts_ops = cntrbtrs_clnts_ops.merge(transaction_features, on='accnt_id', how='left')
    del trnsctns_ops
    df = cntrbtrs_clnts_ops
    df = sklearn.utils.shuffle(df)

    new_df = df.drop(columns=[
        'accnt_bgn_date',  # Неизвестно о каком договоре речь,
        'cprtn_prd_d',  # Аналогично, при предсказании нам неизвестно какой из случаев мы обрабатываем
        # 'erly_pnsn_flg', # Это целевая величина, её нельзя использовать для предсказания
        'brth_yr',  # Возраст человека однозначно определяет его год рождения

        # Эти параметры заменяет почтовый индекс
        'addrss_type',  # Сложные строковый параметр
        'dstrct',  # Множество пропусков
        'city',  # Гигантское кол-во пропусков
        'sttlmnt',  # Гигантское кол-во пропусков
        'brth_plc',  # Большое кол-во различных категориональных призрнаков запутает модель

        'assgn_npo',
        'assgn_ops',


        'accnt_status',  # Эти данные практически хранят ответ
        'prvs_npf',  # Эти данные врядли влияют на результат
        'slctn_nmbr',  # Эта информация не помогает, поскольку о выборке нет дополнительной информации
        'clnt_id',  # Модель не должна зависеть от id клиента
        'accnt_id',
        'phn', 'phn_missing',
        'email', 'email_missing',
        'lk', 'brth_plc_missing'
    ])

    new_df = pd.get_dummies(new_df, columns=['gndr'], drop_first=True)
    new_df["gndr_м"] = new_df["gndr_м"].astype("int32")
    new_df.rename(columns={"gndr_м": "gen"}, inplace=True)

    for col in ['avg_sum_3M', "std_sum_3M", "transaction_freq_3M", "avg_sum_6M", "std_sum_6M", "transaction_freq_6M"]:
        new_df[col] = new_df[col].fillna(0)

    for col in ['rgn']:
        new_df[col] = new_df[col].fillna("Unknown")

    return new_df
