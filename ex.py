from abc import ABC, abstractmethod
from craete_table import PostgresAbc

class Dataaccessor(ABC):
    @abstractmethod
    def get_all_record(self, tablename, column: list, query):
        pass

    @abstractmethod
    def insert_record(self, tablename, column: list, query):
        pass
    
    @abstractmethod
    def delete_record(self, tablename, column: list, query):
        pass
    
    @abstractmethod
    def update_record(self, tablename, column: list, query):
        pass



class PostgresDataaccessor(Dataaccessor):
    def __init__(self):
        super().__init__()
        self.__connection = PostgresAbc()

    def get_all_record(self, tablename, column: list, query):
        self.__cursor.execute(""" 
            select column from tablename
        """%()) 
        users = self.__cursor.fetchall()
        self.__connection.close()

    def insert_record(self, tablename, column: list, query):
        self.__cursor.execute("""
            insert into (tablename) (name) values ('%s')
        """%(column, tablename ))
        self.__connection.commit()
        self.__connection.close()
    
    def delete_record(self, tablename, column: list, query):
        return super().delete_record(tablename, column, query)
    
    def update_record(self, tablename, column: list, query):
        return super().update_record(tablename, column, query)
    

if __name__ == '__main__':
    dataaccessor = PostgresDataaccessor()

    dataaccessor.get_all_record(tablename="", column=[],query='' )    


# class MainClass(ABC):
#     def method_father(self):
#         print("i'm a father")
#     @abstractmethod
#     def abstract_method(self):
#         pass

# class Abstract_realization(MainClass):
#     def abstract_method(self):
#         print ("blablabla")


# ar = Abstract_realization()
# ar.method_father()
# ar.abstract_method()


