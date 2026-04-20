import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exceptions.exception import CustomException
from src.logging.logger_module import logging
from src.entities.config_entity import DataIngestionConfig, GeneralConfig
from src.database.mongo import get_client
from src.entities.artifact_entity import DataIngestionOutput

general_config = GeneralConfig()


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig(general_config)

    def initiate_ingestion(self):
        try:
            logging.info("Starting data ingestion from MongoDB")

            client = get_client()
            db = client[self.config.database_name]
            collection = db[self.config.collection_name]

            logging.info(
                f"Fetching data from DB: {self.config.database_name}, "
                f"Collection: {self.config.collection_name}"
            )

            data = list(collection.find())
            df = pd.DataFrame(data)

            logging.info(f"Data fetched successfully. Shape: {df.shape}")

            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)
                logging.info("_id column dropped")

            return df

        except Exception as e:
            logging.error("Error occurred during data ingestion")
            raise CustomException(e, sys)

    def split_data(self):
        try:
            logging.info("Starting data splitting process")

            data = self.initiate_ingestion()

            logging.info("Saving raw data to feature store")
            data.to_csv(self.config.feature_store_file_path, index=False)

            logging.info("Performing train-test split")
            train, test = train_test_split(
                data,
                test_size=self.config.split_ratio
            )

            logging.info(
                f"Train shape: {train.shape}, Test shape: {test.shape}"
            )

            logging.info("Saving train and test datasets")
            train.to_csv(self.config.training_file_path, index=False)
            test.to_csv(self.config.test_file_path, index=False)

        except Exception as e:
            logging.error("Error occurred during data splitting")
            raise CustomException(e, sys)
   
    def run_data_ingestion(self) -> DataIngestionOutput:
        try:
            logging.info("Running complete data ingestion pipeline")

            self.split_data()

            data_ingestion_output = DataIngestionOutput()
            data_ingestion_output.train_path = self.config.training_file_path,
            data_ingestion_output.test_path = self.config.test_file_path

            logging.info("Data ingestion pipeline completed successfully")

            return data_ingestion_output

        except Exception as e:
            logging.error("Error in run_data_ingestion")
            raise CustomException(e, sys)
            
if __name__ == "__main__":
    obj = DataIngestion()
    output = obj.run_data_ingestion()


        
        
