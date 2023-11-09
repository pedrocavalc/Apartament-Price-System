from abc import abstractmethod
import pandas as pd
class SpliterDataPipeline:
    def __init__(self):
        pass

    def run(self, path):
        try:
            data = pd.read_csv(path, delimiter=';',encoding="ISO-8859-1")
            data = self.clean_data(data)
            data_list = self.split_data(data)
            self.save_data(data_list)
        except Exception as e:
            raise Exception(f"Error while splitting data: Error {e}")
        
    
    def split_data(self, data):
        df_split_1 = data[:int(len(data)/5)]
        df_split_2 = data[int(len(data)/5):int(len(data)/5)*2]
        df_split_3 = data[int(len(data)/5)*2:int(len(data)/5)*3]
        df_split_4 = data[int(len(data)/5)*3:int(len(data)/5)*4]
        df_split_5 = data[int(len(data)/5)*4:]
        return [df_split_1, df_split_2, df_split_3, df_split_4, df_split_5]

    
    def load_data(self, path):
        pd.read_csv(path)


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
    
    def save_data(self, data_list):
        for i, data in enumerate(data_list):
            data.to_csv(f'../../data/interim/split_data_{i}.csv', index=False)