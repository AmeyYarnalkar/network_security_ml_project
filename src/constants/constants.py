from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent

print(BASE)

DATABASE_NAME = "NetworkSecurity"
COLLECTION_NAME = "phishing_data"
