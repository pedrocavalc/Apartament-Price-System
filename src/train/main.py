from trainer.trainer_orchestrator import TrainerOrchestrator



def main(data_path, target):
    trainer = TrainerOrchestrator(data_path, target)
    trainer.run()




if __name__ == "__main__":
    main(data_path="../../data/interim/split_data_0.csv", target="price")