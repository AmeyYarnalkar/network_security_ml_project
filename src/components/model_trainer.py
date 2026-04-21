import sys

from src.exceptions.exception import CustomException
from src.logging.logger_module import logging
from src.entities.config_entity import ModelTrainerConfig, GeneralConfig
from src.entities.artifact_entity import (
    DataTransformationOutput,
    ModelTrainerOutput,
    ClassificationMetric
)
from src.utils.util import load_np_array, save_model, get_classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier
)

from scipy.stats import randint, uniform
from sklearn.model_selection import RandomizedSearchCV


#  Parameter distributions
PARAM_DISTS = {
    "logistic_regression": {
        "C": uniform(0.01, 10),
        "penalty": ["l2"],
        "solver": ["lbfgs"]
    },
    "knn": {
        "n_neighbors": randint(3, 15),
        "weights": ["uniform", "distance"],
        "metric": ["euclidean", "manhattan"]
    },
    "decision_tree": {
        "criterion": ["gini", "entropy"],
        "max_depth": randint(3, 20),
        "min_samples_split": randint(2, 10),
        "min_samples_leaf": randint(1, 5)
    },
    "random_forest": {
        "n_estimators": randint(50, 200),
        "max_depth": randint(5, 20),
        "min_samples_split": randint(2, 10),
        "min_samples_leaf": randint(1, 5),
        "bootstrap": [True, False]
    },
    "adaboost": {
        "n_estimators": randint(50, 200),
        "learning_rate": uniform(0.01, 1)
    },
    "gradient_boosting": {
        "n_estimators": randint(50, 200),
        "learning_rate": uniform(0.01, 0.5),
        "max_depth": randint(3, 10),
        "subsample": uniform(0.5, 0.5)
    }
}


#  Models
MODELS = {
    "logistic_regression": LogisticRegression(max_iter=1000),
    "knn": KNeighborsClassifier(),
    "decision_tree": DecisionTreeClassifier(),
    "random_forest": RandomForestClassifier(),
    "adaboost": AdaBoostClassifier(),
    "gradient_boosting": GradientBoostingClassifier()
}

general_config = GeneralConfig()


class ModelTrainer:
    def __init__(self, data_transformation_output: DataTransformationOutput):
        self.data_transformation_output = data_transformation_output
        self.config = ModelTrainerConfig(general_config)

    def get_train_and_test(self):
        try:
            train_data = load_np_array(self.data_transformation_output.train_path)
            test_data = load_np_array(self.data_transformation_output.test_path)

            x_train = train_data[:, :-1]
            y_train = train_data[:, -1]

            x_test = test_data[:, :-1]
            y_test = test_data[:, -1]

            return x_train, y_train, x_test, y_test

        except Exception as e:
            raise CustomException(e, sys)

    def train_model(self):
        try:
            logging.info("Starting model training")

            x_train, y_train, x_test, y_test = self.get_train_and_test()

            model_report = {}

            #  Train + Tune models
            for name, model in MODELS.items():
                logging.info(f"Training {name}")

                search = RandomizedSearchCV(
                    estimator=model,
                    param_distributions=PARAM_DISTS[name],
                    cv=5,
                    n_iter=20,
                    scoring="f1",
                    n_jobs=-1,
                    random_state=42
                )

                search.fit(x_train, y_train)

                best_model = search.best_estimator_

                y_pred = best_model.predict(x_test)

                report: ClassificationMetric = get_classification_report(y_test, y_pred)

                model_report[name] = {
                    "metric": report,
                    "model": best_model,
                    "best_params": search.best_params_
                }

                logging.info(f"{name} best params: {search.best_params_}")

            #  Select best model
            best_model_name = self.get_best_model(model_report)
            best_model = model_report[best_model_name]["model"]

            logging.info(f"Best model selected: {best_model_name}")

            #  Save model
            save_model(best_model, self.config.model_object_path)

            #  Final evaluation
            train_pred = best_model.predict(x_train)
            test_pred = best_model.predict(x_test)

            result = ModelTrainerOutput(
                trained_model_path=self.config.model_object_path,
                train_classification_metrics=get_classification_report(y_train, train_pred),
                test_classification_metrics=get_classification_report(y_test, test_pred)
            )

            logging.info("Model training completed")

            return result

        except Exception as e:
            raise CustomException(e, sys)

    def get_best_model(self, model_report: dict):
        try:
            best_model = None
            best_score = -1

            for name, info in model_report.items():
                metric = info["metric"]

                if metric.f1_score > best_score:
                    best_score = metric.f1_score
                    best_model = name

            return best_model

        except Exception as e:
            raise CustomException(e, sys)