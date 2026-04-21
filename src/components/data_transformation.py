import sys
import pandas as pd

from src.exceptions.exception import CustomException
from src.logging.logger_module import logging
from src.entities.config_entity import DataTransformationConfig, GeneralConfig
from src.entities.artifact_entity import DataTransformationOutput, DataValidationOutput
from sklearn.impute import SimpleImputer
from src.utils.util import save_model, save_np_array

general_config = GeneralConfig()


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig(general_config)

    def run_transformation(self, output: DataValidationOutput):
        try:
            logging.info("Starting data transformation")

            x_train, y_train, x_test, y_test = self.get_data(
                output.valid_train_file_path,
                output.valid_test_file_path
            )

            #  Handle missing values FIRST
            imputer = SimpleImputer(strategy="most_frequent")

            x_train = imputer.fit_transform(x_train)
            x_test = imputer.transform(x_test)

            #  Then convert to int
            x_train = x_train.astype("int64")
            x_test = x_test.astype("int64")

            y_train = y_train.astype("int64")
            y_test = y_test.astype("int64")

            #  Save preprocessor
            save_model(imputer, self.config.preprocessor_path)

            #  Combine X and y before saving
            train_arr = pd.concat([pd.DataFrame(x_train), y_train.reset_index(drop=True)], axis=1)
            test_arr = pd.concat([pd.DataFrame(x_test), y_test.reset_index(drop=True)], axis=1)

            save_np_array(train_arr.values, self.config.transformed_train_file_path)
            save_np_array(test_arr.values, self.config.transformed_test_file_path)

            logging.info("Data transformation completed")

            return DataTransformationOutput(
                train_path=self.config.transformed_train_file_path,
                test_path=self.config.transformed_test_file_path,
                preprocessor_path=self.config.preprocessor_path
            )

        except Exception as e:
            raise CustomException(e, sys)

    def get_data(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            #  Correct splitting
            x_train = train_df.drop("Result", axis=1)
            y_train = train_df["Result"]

            x_test = test_df.drop("Result", axis=1)
            y_test = test_df["Result"]

            return x_train, y_train, x_test, y_test

        except Exception as e:
            raise CustomException(e, sys)