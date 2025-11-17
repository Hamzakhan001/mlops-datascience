from src.mlops_pipeline import logger
from src.mlops_pipeline.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"{STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    
except Exception as e:
    logger.exception(e)
    raise e