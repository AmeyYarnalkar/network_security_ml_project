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