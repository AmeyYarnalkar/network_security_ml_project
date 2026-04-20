from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent

DATABASE_NAME = "NetworkSecurity"
COLLECTION_NAME = "phishing_data"

DATA_INGESTION_DATABASE_NAME:str = "NetworkSecurity"
DATA_INGESTION_COLLECTION_NAME:str = "phishing_data"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
TRAIN_AND_TEST_SPLIT_RATIO:float = 0.2

TARGET_COLUMN:str = "result"
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR:str = "artifacts"
FILE_NAME:str = "network_data.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

