import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DB_NAME: str
    DB_PORT: str 
    DB_HOST: str 
    
    async def reload_env(self):
        load_dotenv(override=True)

    @property
    async def DATABASE_URL_mongodb(self):
        self.reload_env()
        return f"mongodb://{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"

settings = Settings()