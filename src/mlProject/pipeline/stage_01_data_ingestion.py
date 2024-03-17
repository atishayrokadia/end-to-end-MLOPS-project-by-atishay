from mlProject.config.configuration import ConfigerationManager
from mlProject.components.data_ingestion import DataInestion
from mlProject import logger

STAGE_NAME =  "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init(self):
        pass
    
    def main(self):
        config = ConfigerationManager()
        data_ingestion_config =  config.get_data_ingestion_config()
        data_ingestion = DataInestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj =  DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e