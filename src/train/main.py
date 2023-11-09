from trainer.trainer_orchestrator import TrainerOrchestrator



def main(data_path, target, columns = None):
    trainer = TrainerOrchestrator(data_path, target,columns= columns)
    trainer.run()




if __name__ == "__main__":
    columns = ["currency","fee","pets_allowed","category","cityname","price_type","state","bathrooms","bedrooms","square_feet","price"]
    main(data_path="../../data/interim/split_data_0.csv", target="price", columns = columns)
