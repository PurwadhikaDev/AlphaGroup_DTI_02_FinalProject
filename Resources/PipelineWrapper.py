from sklearn.base import BaseEstimator, TransformerMixin


class PipelineWrapper(BaseEstimator, TransformerMixin):
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def fit(self, X, y=None):
        self.pipeline.fit(X, y)
        return self

    def transform(self, X):
        return self.pipeline.transform(X)
