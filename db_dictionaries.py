'''
Author: Logan Maupin
Date: 10/17/2023

This module is just a collection of database dictionaries that housing the column names
and their respective data_tables for each table. 
'''

video_metadata = {

    # table name
    "table_name": "video_info",

    # column headers : SQL data type
    "date_posted": "text",
    "id": "text",
    "url": "text",
    "title": "text",
    "description": "text",
    "tags": "text[]",
    "duration": "integer",

}

video_transcription_data = {

    # table name
    "table_name": "transcription_data",

    # column headers : SQL data type
    "id": "text",
    "part_number": "integer",
    "transcription_text": "jsonb",

}
