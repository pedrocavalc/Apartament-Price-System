from trainer.components.dataloader.dataloader import DataLoader
from trainer.components.models.modelsManager.models_manager import ModelsManager
from trainer.components.models.pipeline.custom_pipeline import CustomPipeline
from trainer.components.models.modelsConfigurations.models_configuration import ModelsConfiguration
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import mlflow

import warnings
warnings.filterwarnings("ignore")


class TrainerOrchestrator():
    def __init__(self, data_path, target, columns):
        self.data_path = data_path
        self.target = target
        self.columns= columns

    def run(self):
        data_loader = self.get_data_loader()
        models_to_train = self.get_models()
        self.train(data_loader,models_to_train)

    
    def get_data_loader(self):
        data_loader = DataLoader(self.data_path, self.target,self.columns)
        data_loader.run()
        return data_loader
    
    def get_models(self):
        models_to_train = ModelsManager().get_models_dict()
        return models_to_train

    def train(self, data_loader,models_to_train):
        mlflow.start_run()
        mlflow.sklearn.autolog()
        for model_name, model in models_to_train.items():
            grid_search = GridSearchCV(model, ModelsConfiguration().get_parameters(model_name), cv=5, n_jobs=-1, verbose=2,refit=True)
            model = CustomPipeline().build_model(grid_search, data_loader.get_categorical_columns(), data_loader.get_numerical_columns())
            model.fit(data_loader.get_train_data()[0], data_loader.get_train_data()[1])
            self.get_metrics(model, data_loader)

    def get_metrics(self, model, data_loader):
        y_hat = model.predict(data_loader.get_test_data()[0])
        y_true = data_loader.get_test_data()[1]
        mse = mean_squared_error(y_true, y_hat)
        mae = mean_absolute_error(y_true, y_hat)
        r2 = r2_score(y_true, y_hat)
        mlflow.log_metric('mse',mse)
        mlflow.log_metric('mae',mae)
        mlflow.log_metric('r2',r2)

        