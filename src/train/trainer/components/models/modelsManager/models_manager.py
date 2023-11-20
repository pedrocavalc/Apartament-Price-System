from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor

class ModelsManager():
    def __init__(self) -> None:
        self.model_dict = {
                           #"LinearRegression": LinearRegression(), 
                           "RandomForestRegressor": RandomForestRegressor(), 
                           #"MLPRegressor": MLPRegressor(),
                           }
    def get_models_dict(self):
        return self.model_dict