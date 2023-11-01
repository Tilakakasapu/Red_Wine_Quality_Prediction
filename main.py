from src.mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline
from mlproject.pipeline.stage03_data_transforamation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_04_model_trainer import ModeltrainerTrainingPipeline
from mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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

STAGE_NAME = "model training stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = ModeltrainerTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "model evaluation  stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
