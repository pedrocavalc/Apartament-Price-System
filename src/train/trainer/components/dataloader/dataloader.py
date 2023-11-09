from abc import abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader():
    def __init__(self,path, target,columns) -> None:
        self.path = path
        self.target = target
        self.columns = columns
    
    def run(self) -> pd.DataFrame:
        try:
            data = self.load_data()
            data = self.select_columns(data, self.columns)
            self.split_data(data)
            self.get_type_data()
            print(f"The data has been loaded {data.shape}")
        except Exception as e:
            print(f"Error while loading data {e}")

    def load_data(self,) -> pd.DataFrame:
        data = pd.read_csv(self.path)
        return data
    
    def split_data(self, data: pd.DataFrame) -> pd.DataFrame:
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(data.drop(self.target, axis=1), data[self.target], test_size=0.2, random_state=42)

    def get_train_data(self):
        return self.X_train, self.y_train   
    
    def get_test_data(self):
        return self.X_test, self.y_test
    
    def select_columns(self, data, columns):
        if columns:
            data = data.loc[:,columns]
        return data
    
    def get_type_data(self, ):
        self.categorical_columns = []
        self.numerical_columns = []
        for column in self.X_train.columns:
            if self.X_train[column].dtype == "object" or self.X_train[column].dtype == "bool":
                self.categorical_columns.append(column)
            else:
                self.numerical_columns.append(column)

    def get_categorical_columns(self):
        return self.categorical_columns
    
    def get_numerical_columns(self):
        return self.numerical_columns