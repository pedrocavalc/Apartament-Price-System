from trainer.components.dataloader.dataloader import DataLoader
from trainer.components.models.modelsManager.models_manager import ModelsManager
from trainer.components.models.pipeline.custom_pipeline import CustomPipeline

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
        for model_name, model in models_to_train.items():
            model = CustomPipeline().build_model(model, data_loader.get_categorical_columns(), data_loader.get_numerical_columns())
            print(data_loader.get_train_data()[0].isnull().sum())
            model.fit(data_loader.get_train_data()[0], data_loader.get_train_data()[1])


