from src.mlops_pipeline import logger
from src.mlops_pipeline.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlops_pipeline.pipeline.data_validation_pipeline import DataValidationPipeline
from src.mlops_pipeline.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.mlops_pipeline.pipeline.mode_trainer_pipeline import ModeltrainerTrainingPipeline
from src.mlops_pipeline.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

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

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"{STAGE_NAME}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f"{STAGE_NAME}")
    model_transformation = ModeltrainerTrainingPipeline()
    model_transformation.initiate_model_training()
    
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f"{STAGE_NAME}")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    
except Exception as e:
    logger.exception(e)
    raise e