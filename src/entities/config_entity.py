from src.constants import constants as const

class GeneralConfig:
    def __init__(self):
        self.pipeline_name = const.PIPELINE_NAME
        self.artifact_name = const.ARTIFACT_DIR
        self.artifact_dir_path = const.BASE / const.ARTIFACT_DIR


class DataIngestionConfig:
    def __init__(self, config: GeneralConfig):

        #  Root directory
        self.data_ingestion_dir_path = (
            config.artifact_dir_path / const.DATA_INGESTION_DIR_NAME
        )
        self.data_ingestion_dir_path.mkdir(parents=True, exist_ok=True)

        #  Feature store directory
        self.feature_store_dir = (
            self.data_ingestion_dir_path
            / const.DATA_INGESTION_FEATURE_STORE_DIR
        )
        self.feature_store_dir.mkdir(parents=True, exist_ok=True)

        #  Ingested directory
        self.ingested_dir = (
            self.data_ingestion_dir_path
            / const.DATA_INGESTION_INGESTED_DIR
        )
        self.ingested_dir.mkdir(parents=True, exist_ok=True)

        #  File names (just names, no mkdir)
        self.raw_file_name = const.FILE_NAME
        self.train_file_name = const.TRAIN_FILE_NAME
        self.test_file_name = const.TEST_FILE_NAME

        #  Full file paths
        self.feature_store_file_path = self.feature_store_dir / self.raw_file_name
        self.training_file_path = self.ingested_dir / self.train_file_name
        self.test_file_path = self.ingested_dir / self.test_file_name

        #  Other configs
        self.split_ratio = const.TRAIN_AND_TEST_SPLIT_RATIO
        self.database_name = const.DATABASE_NAME
        self.collection_name = const.COLLECTION_NAME
        
class DataValidationConfig(): # inherited because we need ingested data paths
    def __init__(self, config: GeneralConfig):
        #root
        self.data_validation_dir = config.artifact_dir_path / const.DATA_VALIDATION_DIR
        self.data_validation_dir.mkdir(parents=True, exist_ok=True)
        
        #sub directories
        self.valid_data_dir = (self.data_validation_dir / const.VALID_DATA_DIR)
        self.valid_data_dir.mkdir(parents=True, exist_ok=True)
        
        self.invalid_data_dir = (self.data_validation_dir / const.INVALID_DATA_DIR)
        self.invalid_data_dir.mkdir(parents=True, exist_ok=True)
        
        self.drift_dir = (self.data_validation_dir / const.DATA_DRIFT_DIR)
        self.drift_dir.mkdir(parents=True, exist_ok=True)
        
        #file names
        self.valid_train_file_name = const.VALID_TRAIN_FILE_NAME
        self.valid_test_file_name = const.VALID_TEST_FILE_NAME 
        self.drift_file_name = const.DRIFT_FILE_NAME
        
        self.invalid_train_file_name = const.INVALID_TRAIN_FILE_NAME
        self.invalid_test_file_name = const.INVALID_TEST_FILE_NAME  
        
        #full paths
        self.valid_train_file_path = self.valid_data_dir / self.valid_train_file_name
        self.valid_test_file_path = self.valid_data_dir / self.valid_test_file_name
        
        self.invalid_train_file_path = self.invalid_data_dir / self.invalid_train_file_name
        self.invalid_test_file_path = self.invalid_data_dir / self.invalid_test_file_name
        
        self.drift_file_path = self.drift_dir / self.drift_file_name
        
        
class DataTransformationConfig:
    def __init__(self, config: GeneralConfig):
        self.data_transformation_dir = config.artifact_dir_path / const.DATA_TRANSFORMATION_DIR
        self.data_transformation_dir.mkdir(parents=True, exist_ok=True)
        
        self.transformed_train_file_name = const.TRANSFORMED_TRAIN_FILE_NAME.replace("csv","npy")
        self.transformed_test_file_name = const.TRANSFORMED_TEST_FILE_NAME.replace("csv","npy")
        
        self.transformed_train_file_path = self.data_transformation_dir / self.transformed_train_file_name
        self.transformed_test_file_path = self.data_transformation_dir / self.transformed_test_file_name
        self.preprocessor_path = self.data_transformation_dir / const.PREPROCESSOR_OBJECT_NAME
        
class ModelTrainerConfig:
    def __init__(self, config: GeneralConfig):
        self.model_trainer_dir = (config.artifact_dir_path / const.MODEL_TRAINING_DIR)
        self.model_trainer_dir.mkdir(parents=True, exist_ok=True)
        
        self.model_object_path = (self.model_trainer_dir / const.TRAINED_MODEL_OBJECT_NAME)
        self.expected_score = const.MODEL_EXPECTED_SCORE 