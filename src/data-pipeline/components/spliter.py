import pandas as pd
class SpliterDataPipeline:
    def __init__(self):
        pass

    def run(self, path):
        try:
            data = pd.read_csv(path)
            data_list = self.split_data(data)
            self.save_data(data_list)
        except Exception as e:
            raise Exception(f"Error while splitting data: Error {e}")
        
        
    def split_data(data):
        df_split_1 = data[:int(len(data)/5)]
        df_split_2 = data[int(len(data)/5):int(len(data)/5)*2]
        df_split_3 = data[int(len(data)/5)*2:int(len(data)/5)*3]
        df_split_4 = data[int(len(data)/5)*3:int(len(data)/5)*4]
        df_split_5 = data[int(len(data)/5)*4:]
        return [df_split_1, df_split_2, df_split_3, df_split_4, df_split_5]

    def load_data(self, path):
        pd.read_csv(path)
    def save_data(data_list):
        for i, data in enumerate(data_list):
            data.to_csv(f'../../../data/interim/split_data_{i}.csv', index=False)