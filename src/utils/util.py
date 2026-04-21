from src.exceptions.exception import CustomException
from src.logging.logger_module import logging
import sys
import pickle
import yaml
import numpy as np


def read_yaml(file_path):
    try:
        logging.info(f"Attempting to read YAML file from: {file_path}")

        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        if data is None:
            logging.warning(f"YAML file is empty: {file_path}")
            return {}

        logging.info("YAML file read successfully")

        return data

    except Exception as e:
        logging.error(f"Error reading YAML file: {file_path}")
        raise CustomException(e, sys)
    
def save_yaml(data, file_path):
    try:
        if data is None or file_path is None:
            raise CustomException("Data or file path is None", sys)

        logging.info(f"Saving YAML file at: {file_path}")

        with open(file_path, "w") as f:
            yaml.safe_dump(data, f)

        logging.info("YAML file saved successfully")

    except Exception as e:
        logging.error("Error while saving YAML file")
        raise CustomException(e, sys)


# Save model to pickle
def save_model(model, file_path):
    try:
        logging.info(f"Saving model to: {file_path}")

        with open(file_path, "wb") as f:
            pickle.dump(model, f)

        logging.info("Model saved successfully")

    except Exception as e:
        logging.error("Error while saving model")
        raise CustomException(e, sys)


#  Load model from pickle
def load_model(file_path):
    try:
        logging.info(f"Loading model from: {file_path}")

        with open(file_path, "rb") as f:
            model = pickle.load(f)

        logging.info("Model loaded successfully")
        return model

    except Exception as e:
        logging.error("Error while loading model")
        raise CustomException(e, sys)
    
# function to store the np array
def save_np_array(array, file_path):
    try:
        logging.info(f"Saving numpy array to: {file_path}")

        with open(file_path, "wb") as f:
            np.save(f, array)

        logging.info("Numpy array saved successfully")

    except Exception as e:
        logging.error("Error while saving numpy array")
        raise CustomException(e, sys)