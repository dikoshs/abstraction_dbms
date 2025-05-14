from abc import ABC, abstractmethod
import os

import psycopg2
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

    def open_conn(self):
        self.__connection = psycopg2.connect(
            database = "user", 
            user = os.getenv("DATABASE_USER"),
            password = os.getenv("DATABASE_PASSWORD")
            )
        
        self.__cursor=self.__connection.cursor()

    def get_all_record(self, tablename: str, columns: list, where=""):
        columns_str = ', '.join(columns)
        
        if where == None:
            records = self.__execute_query(f""" 
                    select {columns_str} from {tablename} where {where}
            """)
        else:
            records = self.__execute_query(f""" 
                    select {columns_str} from {tablename}
            """)
        return records
    
    def close_conn(self):
        self.__cursor.close()
        self.__connection.close()
    
    def __execute_query(self, query_text: str, commit=False):
        self.open_conn()
        self.__cursor.execute(query_text)
        print("DDDDDDDDDDDDDDDDDDDD ", commit)
        if commit:
            self.__connection.commit()
            self.close_conn()
        else:
            result = self.__cursor.fetchall()
            self.close_conn()
            return result
        


    def insert_record(self, tablename, columns: list, values):
        columns_str = ', '.join(columns)
        records = self.__execute_query(f"""
            insert into {tablename} ({columns_str}) values ('{values}')
        """, commit=True)
        return records
    
    def delete_record(self, tablename, where: dict):
        where_items = ""
        for key, val in where.items():
            if isinstance(val, str):
                where_items += f"{key}='{val}' and"
            else:
                where_items += f"{key}={val} and"
            
        where_items = where_items[:-3]

        self.__execute_query(f"""
            delete from {tablename} where {where_items}                     
        """, commit=True)

    def update_record(self, tablename, columns_values: dict, where: dict):
        set_items = ""
        where_items = ""
        for key, val in columns_values.items():
            if isinstance(val, str):
                set_items += f"{key}='{val}',"
            else:
                set_items += f"{key}={val},"

        set_items = set_items[:-1] 

        for key, val in where.items():
            if isinstance(val, str):
                where_items += f"{key}='{val}' and"
            else:
                where_items += f"{key}={val} and"
            
        where_items = where_items[:-3]

        self.__execute_query(f"""
            update {tablename} set {set_items} where {where_items}
        """, commit=True)


if __name__ == '__main__':
    dataaccessor = PostgresDataaccessor()

    dataaccessor.get_all_record(tablename="users", columns=['name'])    
    dataaccessor.insert_record(tablename="users", columns=['name'], values="blabla")    
    dataaccessor.delete_record(tablename="users", where={
        "name": "blabla"
    })    
    dataaccessor.update_record(tablename="users", columns_values={
        "name": "OOOOO"
    }, where={
        "name": "blabla"
    })    