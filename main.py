from src.mlops_pipeline import logger
from src.mlops_pipeline.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlops_pipeline.pipeline.data_validation_pipeline import DataValidationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"{STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"{STAGE_NAME}")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    
except Exception as e:
    logger.exception(e)
    raise e