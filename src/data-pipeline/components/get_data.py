from urllib import request
import zipfile
import py7zr
import os

class DataManager():
    def __init__(self, url, path) -> None:
        self.url= url
        self.path = path
    
    def get_data(self):
        self.download_data()
        self.unzip_data()
        self.clean_dirs()
        self.load_data()
        self.split_data()

    def download_data(self):
        try:
            response = request.urlretrieve(self.url, f'{self.path}/data_downloaded.zip')
        except Exception as e:
            raise Exception(f"Error while downloading data from url: Error {e}")

    def unzip_data(self):
        with zipfile.ZipFile(f'{self.path}/data_downloaded.zip', 'r') as zip_ref:
            zip_ref.extractall(f'{self.path}')
        with py7zr.SevenZipFile(f'{self.path}/apartments_for_rent_classified_100K.7z', mode='r') as z:
            z.extractall(self.path)

    def clean_dirs(self):
        files = os.listdir(self.path)
        for file in files:
            if file.endswith(".7z") or file.endswith(".zip"):
                os.remove(os.path.join(self.path, file))


def main(url, path):
    dataset_manager = DataManager(url, path)
    dataset_manager.get_data()

if __name__ == "__main__":
    main(url="https://archive.ics.uci.edu/static/public/555/apartment+for+rent+classified.zip", path="../../../data/raw/")