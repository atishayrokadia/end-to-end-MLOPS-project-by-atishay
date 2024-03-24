from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


logger.info("Welcome to our custom log")
print("--------------hi------------------")
STAGE_NAME =  "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion =  DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Pipeline"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation =  DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Model Training Stage"
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
try:
    logger.info(f">>>  stage {STAGE_NAME} started")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nx================x")

except Exception as e:
    logger.exception(e)
    raise e