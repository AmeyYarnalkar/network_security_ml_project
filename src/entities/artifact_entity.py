from dataclasses import dataclass

@dataclass
class DataIngestionOutput:
    train_path:str
    test_path:str
    
@dataclass
class DataValidationOutput:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str
    
@dataclass
class DataTransformationOutput:
    train_path:str
    test_path:str
    preprocessor_path:str
    
@dataclass
class ClassificationMetric:
    f1_score:float
    precision:float
    recall:float
    
@dataclass
class ModelTrainerOutput:
    trained_model_path:str
    train_classification_metrics: ClassificationMetric
    test_classification_metrics: ClassificationMetric
    
