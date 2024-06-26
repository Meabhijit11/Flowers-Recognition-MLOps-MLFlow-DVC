from FlowersRecognition.config.configuration import ConfigurationManager
from FlowersRecognition.components.data_ingestion import DataIngestion
from FlowersRecognition import logger


STAGE_NAME = "Data Ingestion stage"

# Create a class data ingestion pipeline

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

#Create method main and copy pipeline from notebook

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e