import asyncio

from abc import ABC, abstractmethod
from database.database import MongoDBinitialization

class MongodbABC(ABC):
    def __init__(self, db_name: str):
        self.db_name = db_name
        
    @abstractmethod
    async def select(self, column: list, database: str, table: str, query):
        pass

    @abstractmethod
    async def insert(self, column: list, database: str, table: str, query):
        pass

    @abstractmethod
    async def update(self, column: list, database: str, table: str, query):
        pass

    @abstractmethod
    async def delete(self, column: list, database: str, table: str, query):
        pass

    async def log(self, message: str):
        print(f"[{self.db_name}] {message}")


class Mongodb(MongodbABC):
    def __init__(self):
        super().__init__(db_name="MongoDB")
        self._mongodb = None

    async def init_dbms(self):
        self._mongodb = MongoDBinitialization()
        self._mongodb = await self._mongodb.init_mongodb()

    async def select(self, column: list, database: str, table: str, query):
        print("SELECT")
    
    async def insert(self, column: list, database: str, table: str, query):
        print("INSERT")    

    async def update(self, column: list, database: str, table: str, query):
        print("UPDATE")

    async def delete(self, column: list, database: str, table: str, query):
        print("DELETE")
    

async def main():
    mongodb = Mongodb()
    
    await mongodb.init_dbms()

    await mongodb.select(column=[], database="database", table="table", query="asd")
    await mongodb.insert(column=[], database="database", table="table", query="asd")
    await mongodb.update(column=[], database="database", table="table", query="asd")
    await mongodb.delete(column=[], database="database", table="table", query="asd")


if __name__ == '__main__':
    asyncio.run(main())
