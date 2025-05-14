from abc import ABC, abstractmethod
from database.database import MongoDBinitialization

class MongodbABC(ABC):
    async def __init__(self, db_name: str):
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
    async def __init__(self):
        super().__init__(db_name="MongoDB")
        self._connection = MongoDBinitialization()

    async def select(self, column: list, database: str, table: str, query):
        print("SELECT")
    
    async def insert(self, column: list, database: str, table: str, query):
        print("INSERT")    

    async def update(self, column: list, database: str, table: str, query):
        print("UPDATE")

    async def delete(self, column: list, database: str, table: str, query):
        print("DELETE")
    

if __name__ == '__main__':
    mongodb = Mongodb()

    mongodb.select(column=[], database="database", table="table", query="asd")
    mongodb.insert(column=[], database="database", table="table", query="asd")
    mongodb.update(column=[], database="database", table="table", query="asd")
    mongodb.delete(column=[], database="database", table="table", query="asd")
