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

def main():
    client = MongoClient()

    try:        
        client.admin.command('ping')
        print("MongoDB is connected!")
    except Exception as e:
        print("Failed to connect to MongoDB: ", e)

if __name__ == '__main__':
    main()
else:
    mongo_db = MongoDB()