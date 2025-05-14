import psycopg2, os
from dotenv import load_dotenv
# from abc import ABC, abstract

class PostgresAbc():
    def __init__(self):
        load_dotenv(override=True)
        self.__connection = psycopg2.connect(
            database = "user", 
            user = os.getenv("DATABASE_USER"),
            password = os.getenv("DATABASE_PASSWORD")
            )
        self.__cursor=self.__connection.cursor()
        self.create_table()
        
    def create_table(self):
        self.__cursor.execute(""" 
            create table users (
                id serial primary key,
                name varchar (50),
                email varchar(50)
            ); 
        """)
        self.__connection.commit()

postgres = PostgresAbc()
