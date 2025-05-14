import inspect

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie

from core.config import settings
from model import model


class MongoDBinitialization:
    def __init__(self):
        pass

    async def init_mongodb(self):
        self.__client = AsyncIOMotorClient(await settings.DATABASE_URL_mongodb)
        self._database = self.__client[settings.DB_NAME]

        await self.examination_connection()
        await self.create()

        print("MongoDB is connected and initialized")
        

    async def create(self):
        self._document_models = [
            getattr(model, model_name)
            for model_name in model.__all__
            if inspect.isclass(
                getattr(model, model_name) and issubclass(getattr(model, model_name), Document)
            )
        ]

        await init_beanie(database=self._database, document_models=self._document_models)


    async def examination_connection(self):
        if not hasattr(model, "__all__"):
            raise ImportError("Not connection")
        