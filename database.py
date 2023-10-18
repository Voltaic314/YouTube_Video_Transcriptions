'''
Author: Logan Maupin
Date: 10/17/2023

This module is designed with the intent of storing our database class object. 
This script uses a PostgreSQL db schema.
'''
import psycopg2
import config
import utils
import db_dictionaries


class Database:

    def __init__(self, dbname, user, password, host, port) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
        self.conn = psycopg2.connect(
        dbname=self.dbname,
        user=self.user,
        password=self.password,
        host=self.host,
        port=self.port
        )

        self.cursor = self.conn.cursor()

    def build_database(self, database_name) -> None:
        # SQL command to create a new database
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        self.conn.commit()
        
    def build_database_table(self, table_name: str, column_dict: dict) -> None:
        column_data_str = utils.parse_dictionary_for_column_data(column_dict)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {column_data_str}")
        self.conn.commit()

    def log_to_DB(self, formatted_tuple: tuple, table_to_add_values_to: str):
        """
        This function takes your tuple of data and logs it to a new entry at the bottom row of
        whatever table you specified.

        Parameters:
        formatted_tuple: tuple containing the info that the user wishes to log to the database.
        table_to_add_values_to: The name of the table in the database that you want to apend an entry to.
        
        Returns: None
        """

        # The if is to make sure there is anything in the tuple at all, otherwise don't log anything to the database.
        if formatted_tuple:
            formatted_string = utils.format_tuple_into_string(formatted_tuple)
            self.cursor.execute(f'INSERT INTO {table_to_add_values_to} VALUES {formatted_string}', formatted_tuple)
            self.conn.commit()


def main():
    # db variables
    dbname = config.database_info["database_name"]
    user = config.database_info["user"]
    password = config.database_info["password"]
    host = config.database_info["host"]
    port = config.database_info["port"]
    db_instance = Database(dbname=dbname, user=user, password=password, 
                           host=host, port=port)
    db_instance.build_database()
    video_data_table_column_info = db_dictionaries.video_metadata
    video_data_table_name = video_data_table_column_info["table_name"]
    transcription_data_table_column_info = db_dictionaries.video_transcription_data
    transcription_data_table_name = transcription_data_table_column_info["table_name"]
    db_instance.build_database_table(table_name=video_data_table_name, 
                                     column_dict=video_data_table_column_info)
    
    db_instance.build_database_table(table_name=transcription_data_table_name, 
                                    column_dict=transcription_data_table_column_info)


if __name__ == "__main__":
    main()
