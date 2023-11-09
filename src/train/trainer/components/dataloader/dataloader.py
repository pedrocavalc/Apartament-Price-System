from abc import abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader():
    def __init__(self,path, target) -> None:
        self.path = path
        self.target = target
    
    def run(self) -> pd.DataFrame:
        try:
            data = self.load_data()
            self.split_data(data)
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