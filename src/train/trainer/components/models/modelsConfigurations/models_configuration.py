class ModelsConfiguration():
    def __init__(self) -> None:
        self.parameters = {
        'LinearRegression': {
        },
        'RandomForestRegressor': {
            'n_estimators': [10, 50, 100, 200],
            'max_features': ['auto', 'sqrt', 'log2'],
            'max_depth': [None, 10, 20, 30, 40, 50],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'bootstrap': [True, False]
        },
        'MLPRegressor': {
            'hidden_layer_sizes': [(50,), (100,100)],
            'activation': ['tanh', 'relu'],
            'solver': [ 'sgd', 'adam'],
            'alpha': [0.0001, 0.1],
            'learning_rate': ['constant', 'adaptive'],
            'max_iter': [200, 400, 800]
        }
    }
        
    def get_parameters(self, model_name):
        return self.parameters[model_name]