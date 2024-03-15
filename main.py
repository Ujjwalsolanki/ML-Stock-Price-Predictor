from logger import logging
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.state_02_model_trainer import ModelTrainerPipeline


STAGE_NAME = "Data Ingestion Pipeline"
try:
    
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    ## Create pipeline object and call it from here
    object = DataIngestionPipeline()
    object.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Model Trainer Pipeline"
try:
    
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    ## Create pipeline object and call it from here
    object = ModelTrainerPipeline()
    object.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e
