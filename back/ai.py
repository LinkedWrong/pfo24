from catboost import CatBoostClassifier


model = CatBoostClassifier()
model.load_model("files/best_tree.cbm")


def predict(x):
    return model.predict(x)
