from catboost import CatBoostClassifier

class Model:
    classifier: CatBoostClassifier

    def __init__(self, *args, **kwargs):
        self.classifier = CatBoostClassifier(*args, **kwargs)

    def fit(self, X, y, *args, **kwargs):
        self.classifier.fit(X, y, *args, **kwargs)

    def predict(self, X):
        return self.classifier.predict(X)

    def load(self, path: str):
        self.classifier.load_model(path)

    def save(self, *args, **kwargs):
        self.classifier.save_model(*args, **kwargs)

