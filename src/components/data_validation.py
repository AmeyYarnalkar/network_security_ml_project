import sys
import pandas as pd
from scipy.stats import ks_2samp

from src.exceptions.exception import CustomException
from src.logging.logger_module import logging
from src.entities.artifact_entity import (
    DataIngestionOutput,
    DataValidationOutput
)
from src.entities.config_entity import DataValidationConfig, GeneralConfig
from src.utils.util import read_yaml, save_yaml
from src.constants.constants import DATA_SCHEMA_FILE_PATH


general_config = GeneralConfig()


class DataValidation:
    def __init__(self, data_ingestion_output: DataIngestionOutput):
        self.data_ingestion_output = data_ingestion_output
        self.config = DataValidationConfig(config=general_config)
        self._schema_config = read_yaml(DATA_SCHEMA_FILE_PATH)

    #  Read data
    def get_df(self) -> tuple:
        try:
            logging.info("Reading train and test datasets")

            train_df = pd.read_csv(self.data_ingestion_output.train_path)
            test_df = pd.read_csv(self.data_ingestion_output.test_path)

            logging.info(
                f"Train shape: {train_df.shape}, Test shape: {test_df.shape}"
            )

            return train_df, test_df

        except Exception as e:
            logging.error("Error while reading datasets")
            raise CustomException(e, sys)

    #  Validate columns + dtype
    def validate_columns(self, df: pd.DataFrame) -> bool:
        try:
            logging.info("Validating schema columns")

            expected_cols = self._schema_config["columns"]

            # Check missing columns
            missing_cols = [col for col,data_type in expected_cols.items() if col not in df.columns]
            if missing_cols:
                raise CustomException(f"Missing columns: {missing_cols}", sys)

            # dtype mapping
            def map_dtype(dtype):
                if "int" in str(dtype):
                    return "int"
                elif "float" in str(dtype):
                    return "float"
                else:
                    return "string"

            # Check data types
            for col, expected_type in expected_cols.items():
                actual_type = map_dtype(df[col].dtype)
                expected_type = map_dtype(expected_type)

                if expected_type != actual_type:
                    raise CustomException(
                        f"{col}: expected {expected_type}, got {actual_type}",
                        sys
                    )

            logging.info("Column validation successful")
            return True

        except Exception as e:
            logging.error("Column validation failed")
            raise CustomException(e, sys)

    #  Drift detection
    def get_drift_report(self, train_df: pd.DataFrame, test_df: pd.DataFrame):
        try:
            logging.info("Starting drift detection using KS test")

            num_cols = self._schema_config["numerical_columns"]
            drift_report = {}

            for col in num_cols:
                stat, p_value = ks_2samp(train_df[col], test_df[col])

                drift_report[col] = {
                    "p_value": float(p_value),
                    "drift_detected": bool(p_value < 0.05)
                }

            logging.info("Drift detection completed")
            return drift_report

        except Exception as e:
            logging.error("Error during drift detection")
            raise CustomException(e, sys)

    # 🔹 Export data
    def handle_export(self, is_valid, train_df, test_df):
        try:
            if is_valid:
                logging.info("Saving VALID datasets")

                train_df.to_csv(self.config.valid_train_file_path, index=False)
                test_df.to_csv(self.config.valid_test_file_path, index=False)

            else:
                logging.info("Saving INVALID datasets")

                train_df.to_csv(self.config.invalid_train_file_path, index=False)
                test_df.to_csv(self.config.invalid_test_file_path, index=False)

        except Exception as e:
            logging.error("Error while saving datasets")
            raise CustomException(e, sys)

    # 🔹 Main pipeline
    def run_data_validation(self) -> DataValidationOutput:
        try:
            logging.info("Starting data validation pipeline")

            train_df, test_df = self.get_df()

            # Validate schema
            self.validate_columns(train_df)
            self.validate_columns(test_df)

            # Drift check
            report = self.get_drift_report(train_df, test_df)

            logging.info("Saving drift report")
            save_yaml(report, self.config.drift_file_path)

            # Check overall drift
            has_valid_distribution = all(
                not col_data["drift_detected"] for col_data in report.values()
            )

            # Export data
            self.handle_export(has_valid_distribution, train_df, test_df)

            logging.info(f"Validation status: {has_valid_distribution}")

            return DataValidationOutput(
                validation_status=has_valid_distribution,
                valid_train_file_path=(
                    self.config.valid_train_file_path if has_valid_distribution else None
                ),
                valid_test_file_path=(
                    self.config.valid_test_file_path if has_valid_distribution else None
                ),
                invalid_train_file_path=(
                    self.config.invalid_train_file_path if not has_valid_distribution else None
                ),
                invalid_test_file_path=(
                    self.config.invalid_test_file_path if not has_valid_distribution else None
                ),
                drift_report_file_path=self.config.drift_file_path
            )

        except Exception as e:
            logging.error("Data validation pipeline failed")
            raise CustomException(e, sys)