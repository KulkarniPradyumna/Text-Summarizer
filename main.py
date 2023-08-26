from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
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
    