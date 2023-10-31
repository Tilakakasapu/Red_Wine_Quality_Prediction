from src.mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline
from mlproject.pipeline.stage03_data_transforamation import DataTransformationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"stage {STAGE_NAME} completed <<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DatavalidationTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e