from abc import ABC, abstractmethod

class MongodbABC(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class Mongodb(MongodbABC):
    def ff(self):
        print("DDDDDDDDDD------")

    def create(self):
        print("create")
    
    def update(self):
        print("update")

    def delete(self):
        print("delete")
    

mongodb = Mongodb()
mongodb.create()
mongodb.update()
mongodb.delete()
