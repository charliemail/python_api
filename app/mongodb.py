# mongodb.py
from pymongo import MongoClient
from envyaml import EnvYAML

class MongoDB:
    def __init__(self):
        # 取得 YAML 檔環境變數參照自 .env 檔
        env = EnvYAML("docker-compose.yml")
        mongo_uri = env['services.mongodb.environment.MONGO_URI']
        mongo_db = env['services.mongodb.environment.MONGO_DB_NAME']

        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]

mongo_db = MongoDB()
