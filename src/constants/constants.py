from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent

DATABASE_NAME = "NetworkSecurity"
COLLECTION_NAME = "phishing_data"

""" Data schema file path"""

DATA_SCHEMA_FILE_PATH = (BASE / "schema" / "data_schema.yaml")

""" Data Ingestion Constants"""

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

"""Data Validation Constants"""

DATA_VALIDATION_DIR:str = "data_validation"
VALID_DATA_DIR:str = "valid"
INVALID_DATA_DIR:str = "invalid"
VALID_TRAIN_FILE_NAME:str = "valid_train.csv"
VALID_TEST_FILE_NAME:str = "valid_test.csv"
INVALID_TRAIN_FILE_NAME:str = "invalid_train.csv"
INVALID_TEST_FILE_NAME:str = "invalid_test.csv"
DATA_DRIFT_DIR:str = "drift"
DRIFT_FILE_NAME:str = "drift_report.yaml"

"""Data Transformation Constants"""

DATA_TRANSFORMATION_DIR:str = "data_transformation"
TRANSFORMED_TRAIN_FILE_NAME = "transformed_train.csv"
TRANSFORMED_TEST_FILE_NAME = "transformed_test.csv"
PREPROCESSOR_OBJECT_NAME = "preprocessor.pkl"

""" Model Training Constants"""

MODEL_TRAINING_DIR:str = "model_trainer"
TRAINED_MODEL_OBJECT_NAME:str = "model.pkl"
MODEL_EXPECTED_SCORE:float = 0.6
