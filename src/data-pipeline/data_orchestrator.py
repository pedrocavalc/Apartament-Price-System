from components.get_data import DataManager
from components.preprocessor import SpliterDataPipeline

class DataOrchestrator:
    def __init__(self,):
        pass

    def run(url, path, id_file):
        data_manager = DataManager(url, path)
        file_path = data_manager.get_data()
        SpliterDataPipeline().run(file_path)

def main(url, path, id_file):
    DataOrchestrator.run(url, path, id_file)

if __name__ == "__main__":
    main(url="https://archive.ics.uci.edu/static/public/555/apartment+for+rent+classified.zip", path="../../data/raw", id_file=0)
