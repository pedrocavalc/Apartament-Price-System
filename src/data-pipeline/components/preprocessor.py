import pandas as pd

class PreProcessor():
    def __init__(self) -> None:
        pass

    def run(self, path):
        data = self.load_data(path)
        data = self.clean_data(data)
        print(data.isnull().sum())
    
    def load_data(self, path):
        data = pd.read_csv(path)
        return data
    
    def clean_data(self, data):
        object_columns = data.select_dtypes(include=['object','bool']).columns
        numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
        for column in data.columns:
            print('replace')
            if column in object_columns:
                data[column].fillna('not_specified', inplace=True)
            if column in numeric_columns:
                data[column].fillna(data[column].mode().iloc[0], inplace=True)

        return data

