from pymongo import MongoClient
from core.config import settings

class MongoDBinitialization:
    def __init__(self):
        pass

    def init_mongodb(self):
        self.__client = MongoClient(settings.DATABASE_URL_mongodb)
        self._database = self.__client[settings.DB_NAME]

        print("MongoDB is connected and initialized")
        return self._database
        