#  Copyright (c) 2022/3/26 By Alireza Soltani Jazi
import mysql.connector


# set global net_buffer_length=1000000;
# set global max_allowed_packet=1000000000;
# SET GLOBAL connect_timeout = 10;
# SHOW VARIABLES LIKE "%timeout";
class MySQLConnector:
    def __init__(self, host: str, username: str, password: str, database: str):
        self._host = host
        self._username = username
        self._password = password
        self._database = database

    def connect_to_mysql(self):
        mydb = mysql.connector.connect(
            host=self._host,
            user=self._username,
            password=self._password,
            database=self._database
        )
        print(f'Connected successfully to the DB:\n{mydb}', flush=True)
        return mydb


class DatabaseHandler:
    def __init__(self, link):
        self._link = link
        self._cursor = link.cursor()

    def create_database(self, new_database_name: str):
        cursor = self._cursor
        cursor.execute(f"create database {new_database_name}")

    def display_all_databases(self):
        cursor = self._cursor
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        for database in databases:
            print(f'Databases: {database}', flush=True)

    def create_table(self, table_name: str, columns: str):
        cursor = super().__getattribute__("_cursor")
        print(f"Query is: CREATE TABLE {table_name} {columns}")
        cursor.execute(f"CREATE TABLE {table_name} {columns}")

    def display_all_tables(self):
        cursor = self._cursor
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            print(f'Tables: {table}', flush=True)

    def insert_data(self, table_name: str, values: list, columns: str):
        cursor = self._cursor
        link = self._link
        columns_len = len(columns.split(','))
        query_value = '%s'
        for column in range(columns_len - 1):
            query_value += ', %s'
        query_value = '(' + query_value + ')'
        query = f"INSERT INTO {table_name} {columns} VALUES {query_value}"
        print(query)
        for item in values:
            cursor.executemany(query, item)
            link.commit()
            print(cursor.rowcount, "records inserted!", flush=True)
        print('All data inserted successfully!')

    def select_table(self, table_name: str, limit: int, offset: int):
        cursor = self._cursor
        query = f"SELECT * FROM {table_name} limit {limit} offset {offset}"
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record, flush=True)
