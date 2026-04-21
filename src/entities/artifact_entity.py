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