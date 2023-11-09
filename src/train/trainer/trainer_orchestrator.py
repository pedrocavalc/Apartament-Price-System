from trainer.components.dataloader.dataloader import DataLoader

class TrainerOrchestrator():
    def __init__(self, data_path, target):
        self.data_path = data_path
        self.target = target

    def run(self):
        data_loader = self.get_data()
        self.train(data_loader)
    
    def get_data(self):
        data_loader = DataLoader(self.data_path, self.target)
        data_loader.run()
        return data_loader
    