from src.components.model_trainer import Model_Trainer


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        model_trainer = Model_Trainer()
        model_trainer.initiate_model_training()


if __name__ == '__main__':
    try:
        obj = ModelTrainerPipeline()
        obj.main()
    except Exception as e:
        raise e

