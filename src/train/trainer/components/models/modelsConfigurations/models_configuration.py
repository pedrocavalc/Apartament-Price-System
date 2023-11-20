class ModelsConfiguration():
    def __init__(self) -> None:
        self.parameters = {
        'LinearRegression': {
        },
        'RandomForestRegressor': {
            'n_estimators': [10,  100, 200],
            'max_depth': [None, 10],
            'min_samples_split': [ 5, 10],
            'min_samples_leaf': [ 2, 4],

        },
        'MLPRegressor': {
            'hidden_layer_sizes': [(50,), (100,100)],
            'activation': ['relu'],
            'solver': [ 'sgd', ],
            'alpha':  [0.1],
            'learning_rate': ['adaptive'],
            'max_iter': [200, 400, 800]
        }
    }
        
    def get_parameters(self, model_name):
        return self.parameters[model_name]