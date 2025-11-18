from src.mlops_pipeline.config.configuration import ConfigurationManager
from src.mlops_pipeline.components.model_trainer import ModelTrainer
from src.mlops_pipeline import logger

STAGE_NAME="Data trainer Stage"


class ModeltrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config= ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        