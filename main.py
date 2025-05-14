import asyncio

from abc import ABC, abstractmethod
from database.database import MongoDBinitialization


class MongodbABC(ABC):
    def __init__(self, db_name: str):
        self.db_name = db_name
    
    @abstractmethod
    def select(self, collection: str, query: dict):
        pass

    @abstractmethod
    def insert(self, collection: str, document: dict):
        pass

    @abstractmethod
    def update(self, collection: str, query: dict, update: dict):
        pass

    @abstractmethod
    def delete(self, collection: str, query: dict):
        pass

    @abstractmethod
    def create(self, collection: str, document: dict):
        pass

    def log(self, message: str):
        print(f"[{self.db_name}] {message}")


class Mongodb(MongodbABC):
    def __init__(self):
        super().__init__(db_name="MongoDB")
        self._mongodb = MongoDBinitialization()
        self._mongodb = self._mongodb.init_mongodb()

    def select(self, collection: str, query: dict):
        cursor = self._mongodb[collection].find(query)
        results = list(cursor)  
        return results
    
    def insert(self, collection: str, document: dict):
        result = self._mongodb[collection].insert_one(document)
        return result.inserted_id
    
    def update(self, collection: str, query: dict, update: dict):
        result = self._mongodb[collection].update_one(query, {"$set": update})
        return result.modified_count
    
    def delete(self, collection: str, query: dict):
        result = self._mongodb[collection].delete_one(query)
        return result.deleted_count

    def create(self, collection: str, document: dict):
        collection_names = self._mongodb.list_collection_names()
        if collection not in collection_names:
            self._mongodb.create_collection(collection)
            print(f"Collection {collection} created.")
        else:
            print(f"Collection {collection} already exists.")

        result = self.insert(collection, document)
        return result


if __name__ == '__main__':
    mongodb = Mongodb()

    collection_name = "users"
    query = {"name": "Alice"}

    created_id = mongodb.create(collection=collection_name, document={"name": "Charlie", "age": 25})
    print("Created Document ID:", created_id)

    results = mongodb.select(collection=collection_name, query=query)
    print("Select Results:", results)

    new_document = {"name": "Bob", "age": 30}
    inserted_id = mongodb.insert(collection=collection_name, document=new_document)
    print("Inserted Document ID:", inserted_id)

    update_query = {"name": "Bob"}
    update_data = {"age": 31}
    modified_count = mongodb.update(collection=collection_name, query=update_query, update=update_data)
    print("Modified Count:", modified_count)

    delete_query = {"name": "Bob"}
    deleted_count = mongodb.delete(collection=collection_name, query=delete_query)
    print("Deleted Count:", deleted_count)