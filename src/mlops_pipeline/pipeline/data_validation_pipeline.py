from src.mlops_pipeline.config.configuration import ConfigurationManager
from src.mlops_pipeline.components.data_validation import DataValidation
from src.mlops_pipeline import logger


STAGE_NAME="Data Validation Stage"


class DataValidationPipeline:
    def __init__(self):
        pass
    
    def initiate_data_validation(self):
        config= ConfigurationManager()
        data_validation_config=config.get_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()