import sys
import pandas as pd

from src.logging.logger_module import logging
from src.exceptions.exception import CustomException
from src.constants.constants import BASE, DATABASE_NAME, COLLECTION_NAME
from src.database.mongo import get_client

file_path = BASE / "Data" / "phisingData.csv"


class ETLPipeline:
    def __init__(self):
        self.client = get_client()

    # Convert CSV → structured JSON (list of dicts)
    def to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)

            # The line `records = df.to_dict(orient="records")` is converting the DataFrame `df` into
            # a list of dictionaries where each dictionary represents a row in the DataFrame.
            records = df.to_dict(orient="records")
            return records

        except Exception as e:
            raise CustomException(e, sys)

    # Insert into MongoDB
    def insert_data(self, records, database, collection):
        try:
            db = self.client[database]
            collection = db[collection]

            result = collection.insert_many(records)

            return len(result.inserted_ids)

        except Exception as e:
            raise CustomException(e, sys)

    # Run full ETL
    def run_etl(self, file_path):
        try:
            records = self.to_json(file_path)
            count = self.insert_data(
                records,
                database=DATABASE_NAME,
                collection=COLLECTION_NAME
            )

            logging.info(f"Inserted {count} records into MongoDB")
            return count

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    etl_pipeline = ETLPipeline()
    length = etl_pipeline.run_etl(file_path=file_path)
    logging.info(f"ETL process is successful for the {length} number of records")