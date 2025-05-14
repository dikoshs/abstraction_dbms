import inspect

from pymongo import MongoClient
from beanie import Document, init_beanie

from core.config import settings
from model import model


class MongoDBConnection:
    def __init__(self):
        self.__client = MongoClient(settings.DATABASE_URL_mongodb)
        self._database = self.__client[settings.DB_NAME]

        self.examination_connection()

        self._document_models = self.initialization()
        init_beanie(database=self._database, document_models=self._document_models)

        print("MongoDB is connected and initialized")


    def initialization(self):
        return [
            getattr(model, model_name)
            for model_name in model.__all__
            if inspect.isclass(
                getattr(model, model_name) and issubclass(getattr(model, model_name), Document)
            )
        ]


    def examination_connection(self):
        if not hasattr(model, "__all__"):
            raise ImportError("Not connection")
        

mongodb_connection = MongoDBConnection()