import sys
import numpy as np

from src.exceptions.exception import CustomException
from src.logging.logger_module import logging


class NetworkModel:
    def __init__(self, preprocessor, model):
        self.preprocessor = preprocessor
        self.model = model

    def predict(self, data):
        try:
            logging.info("Starting prediction")

            #  Ensure input is numpy array
            if not isinstance(data, np.ndarray):
                data = np.array(data)

            #  Reshape if single sample
            if len(data.shape) == 1:
                data = data.reshape(1, -1)

            #  Apply preprocessing
            data_transformed = self.preprocessor.transform(data)

            #  Convert to int (to match training)
            data_transformed = data_transformed.astype("int64")

            #  Predict
            prediction = self.model.predict(data_transformed)

            logging.info("Prediction completed successfully")

            return prediction

        except Exception as e:
            logging.error("Error during prediction")
            raise CustomException(e, sys)