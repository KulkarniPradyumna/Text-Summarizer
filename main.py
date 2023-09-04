from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.logging import logger

stage_name = "Data Ingestion Stage"
try:
    logger.info(f"<<<<<<<stage {stage_name} started >>>>>>>")
    data_ingestion = DataIngestionPipeline
    data_ingestion.main()
    logger.info(f"<<<<<<<stage {stage_name} completed >>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
    
stage_name = "Data Validation Stage"
try:
    logger.info(f"<<<<<<<stage {stage_name} started >>>>>>>")
    data_validation = DataValidationPipeline
    data_validation.main()
    logger.info(f"<<<<<<<stage {stage_name} completed >>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Data Transformation Stage"
try:
    logger.info(f"<<<<<<<stage {stage_name} started >>>>>>>")
    data_transformation = DataTransformationPipeline
    data_transformation.main()
    logger.info(f"<<<<<<<stage {stage_name} completed >>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Model Training Stage"
try:
    logger.info(f"<<<<<<<stage {stage_name} started >>>>>>>")
    model_trainer = ModelTrainingPipeline
    model_trainer.main()
    logger.info(f"<<<<<<<stage {stage_name} completed >>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e