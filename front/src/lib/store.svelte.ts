type Field<T> = {
	name: string;
	type: string;
	value?: T;
	description: string;
};

export type FormData = {
  slctn_nmbr: number;
  clnt_id: string;
  accnt_id: string;
  gndr: string;
  brth_yr: number;
  prsnt_age: number;
  accnt_bgn_date: string;
  cprtn_prd_d: number;
  erly_pnsn_flg: number;
  accnt_status: string;
  pnsn_age: number;
  prvs_npf: string;
  brth_plc: string;
  addrss_type: string;
  rgn: string;
  dstrct: string;
  city: string;
  sttlmnt: string;
  pstl_code: string;
  okato: number;
  phn: string;
  email: string;
  lk: string;
  assgn_npo: string;
  assgn_ops: string;
}

export const formFields: Field<string | number>[] = [
	{
		name: 'slctn_nmbr',
		type: 'number',
		description: 'Номер выборки'
	},
	{
		name: 'clnt_id',
		type: 'string',
		description: 'ID клиента'
	},
	{
		name: 'accnt_id',
		type: 'string',
		description: 'ID счета клиента'
	},
	{
		name: 'gndr',
		type: 'string',
		description: 'Пол клиента'
	},
	{
		name: 'brth_yr',
		type: 'number',
		description: 'Год рождения клиента'
	},
	{
		name: 'prsnt_age',
		type: 'number',
		description: 'Возраст клиента на текущий год'
	},
	{
		name: 'accnt_bgn_date',
		type: 'string',
		description: 'Дата заключения договора'
	},
	{
		name: 'cprtn_prd_d',
		type: 'number',
		description:
			'Время между датой заключения договора и датой статуса договора, дни. Для вышедших на пенсию («выплатной период») этот период соответствует времени взаимодействия клиентов с фондом (от даты заключения договора до даты назначения пенсии). Для клиентов в накопительном периоде это время, прошедшее между датой заключения договора и датой начала платежей на счет клиента'
	},
	{
		name: 'erly_pnsn_flg',
		type: 'number',
		description:
			'Целевая переменная. 0, 1 – маркер досрочного выхода на пенсию. Указывает вышел ли клиент на пенсию в возрасте, установленном законами РФ (0) или же раньше стандартного возраста (1). Маркером 0 отмечены клиенты в накопительном периоде, возраст которых больше возраста выхода на пенсию, установленного законами РФ'
	},
	{
		name: 'accnt_status',
		type: 'string',
		description: 'Статус счета/договора'
	},
	{
		name: 'pnsn_age',
		type: 'number',
		description: 'Возраст выхода на пенсию согласно закону РФ'
	},
	{
		name: 'prvs_npf',
		type: 'string',
		description: 'Предыдущий НПФ, с которым сотрудничал клиент до перехода к нам'
	},
	{
		name: 'brth_plc',
		type: 'string',
		description: 'Место рождения клиента'
	},
	{
		name: 'addrss_type',
		type: 'string',
		description: 'Тип адреса указанного клиентом'
	},
	{
		name: 'rgn',
		type: 'string',
		description: 'Регион, указанный клиентом'
	},
	{
		name: 'dstrct',
		type: 'string',
		description: 'Район, указанный клиентом'
	},
	{
		name: 'city',
		type: 'string',
		description: 'Город, указанный клиентом'
	},
	{
		name: 'sttlmnt',
		type: 'string',
		description: 'Населенный пункт, указанный клиентом'
	},
	{
		name: 'pstl_code',
		type: 'string',
		description: 'Почтовый индекс'
	},
	{
		name: 'okato',
		type: 'number',
		description: 'Код ОКАТО'
	},
	{
		name: 'phn',
		type: 'string',
		description: 'Маркер наличия телефона'
	},
	{
		name: 'email',
		type: 'string',
		description: 'Маркер наличия email'
	},
	{
		name: 'lk',
		type: 'string',
		description: 'Маркер регистрации в ЛКК'
	},
	{
		name: 'assgn_npo',
		type: 'string',
		description: 'Маркер является ли клиент правопреемником по договору'
	},
	{
		name: 'assgn_ops',
		type: 'string',
		description: 'Маркер является ли клиент правопреемником по договору ОПС'
	}
];
