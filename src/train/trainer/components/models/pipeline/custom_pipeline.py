from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class CustomPipeline():
    def __init__(self) -> None:
        pass

    def build_model(self, model, categorical_columns, numerical_columns):
        cat_pipline = OneHotEncoder(handle_unknown='ignore')
        numerical_pipeline = StandardScaler()
        column_transform = ColumnTransformer([('categorical_pipeline', cat_pipline, categorical_columns ), ('numerical_pipeline', numerical_pipeline, numerical_columns)])
        return Pipeline([('column_transform', column_transform), ('regressor', model)])
