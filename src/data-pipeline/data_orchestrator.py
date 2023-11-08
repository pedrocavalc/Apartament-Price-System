from components.get_data import DataManager
from components.spliter import SpliterDataPipeline

class DataOrchestrator:
    def __init__(self, source, destination):
        pass

    def run(url, path):
        data_manager = DataManager(url, path)
        data_manager.get_data()
        SpliterDataPipeline().run(path)


def main(url, path):
    DataOrchestrator.run(url, path)

if __name__ == "__main__":
    main(url="https://archive.ics.uci.edu/static/public/555/apartment+for+rent+classified.zip", path="../../../data/raw/")
