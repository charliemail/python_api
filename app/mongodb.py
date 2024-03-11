# mongodb.py
from pymongo import MongoClient
from app.config import MongoDBConfig

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MongoDBConfig.URI)
        self.db = self.client[MongoDBConfig.DB_NAME]

mongo_db = MongoDB()
