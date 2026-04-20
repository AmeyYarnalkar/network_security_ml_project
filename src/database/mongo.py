from pymongo import MongoClient
from dotenv import load_dotenv
from src.exceptions.exception import CustomException
import os

load_dotenv()

def get_client():
    uri = os.getenv("MONGO_URI")
    
    if not uri:
        raise CustomException("MONGO_URI not found in environment variables")
    
    return MongoClient(uri)


# Only run when file is executed directly
if __name__ == "__main__":
    client = get_client()
    print(client.list_database_names())