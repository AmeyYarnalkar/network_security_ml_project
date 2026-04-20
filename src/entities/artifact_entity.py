from dataclasses import dataclass

@dataclass
class DataIngestionOutput:
    train_path:str
    test_path:str