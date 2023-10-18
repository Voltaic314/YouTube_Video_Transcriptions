'''
Author: Logan Maupin
Date: 10/17/2023

This module is really just an un-organized collection of utility functions I can use
to help build my database and insert specific types of data into these tables.
'''
import json


def parse_dictionary_for_column_data(columns_dict: dict[str, str]) -> str:
    '''
    This function takes a dictionary of column data that you wish to create 
    SQL table columns for. You must pass in a dictionary where the keys are going
    to be the column titles, and the values will be what type of data they are. 
    like this... {"Username": "text"} where Username will be the column title and
    text is its type of data it will hold in that column. 

    Parameters:
    columns_dict: a dictionary where the keys represent column names (strings) and 
    the values repesent their data types (strings also).

    Returns: formatted string that can be used to pass into SQL cursor commands to 
    create tables.
    '''
    if not columns_dict:
        return ''
    
    formatted_output_string = ''
    for key, value in columns_dict.items():
        if len(columns_dict) == 1:
            return f'({key} {value})'

        elif len(columns_dict) > 1:
            last_key_of_dict = columns_dict.items()[-1][0]
            if key == last_key_of_dict and key != "table_name":
                formatted_output_string += f'({key} {value})'

            else:
                formatted_output_string += f'({key} {value}, '

    return formatted_output_string


def format_list_into_sql_array(input_list: list) -> str:
    '''
    This function takes a list of values like this: 
    ["hi", "hello"] 
    and converts that to a sql one dimensional array data type like this:
    {"hi", "hello"}
    Specifically it converts it to a string that looks like that so it can be
    passed into sql cursor commands.

    Parameters:
    input_list: a list of value that you wish to have formatted

    Returns: a formatted string ideally for PostgreSQL 1d array column data types.
    '''
    formatted_output_string = '{' + '}'
    
    if not input_list:
        return formatted_output_string
    
    if len(input_list) == 1:
        
        formatted_output_string += '{' + str(input_list[0]) + '}'
        return formatted_output_string
    
    elif len(input_list) > 1:
        
        for i in range(len(input_list)):
            item_in_list = input_list[i]
            formatted_output_string += '{' + str(item_in_list) + '}'
        
            if i != len(input_list) - 1:
                formatted_output_string += ','
        
        return formatted_output_string
    

def format_tuple_into_string(formatted_tuple: tuple):
    """
    THe purpose of this function is to take a tuple of items in any order and create a (?) or (?, ?), kind of string
    that can be inserted into sql statement strings like the insert into database kind of strings.
    
    Parameters: 
    formatted_tuple: tuple containing the info that the user wishes to log to the database.
    
    
    Returns: Formatted string to be used for the sql insertion string.
    """

    # The if is to make sure there is anything in the tuple at all, otherwise don't log anything to the database.
    if formatted_tuple:
        if len(formatted_tuple) > 1:
            formatted_string = "("
            formatted_string += "?, " * (len(formatted_tuple) - 1)
            formatted_string += "?)"
            return formatted_string

        elif len(formatted_tuple) == 1:
            formatted_string = "(?)"
            return formatted_string


def format_publish_date_to_str(publish_date: object) -> str:
    '''
    This function takes a datetime object and pulls out its methods to 
    add into a formatted string.

    Parameters: 
    publish_date: datetime object from the datetime library in Python

    Returns: formatted string like "dd-mm-yyyy"
    '''
    return f'{publish_date.day}-{publish_date.month}-{publish_date.year}'


def convert_string_to_json_dict(json_string: str) -> dict:
    '''
    Using the json dumps function from the json library to convert a string
    to a dictionary object. :) 

    Parameters: 
    json_string: str data type in the format of a flattened json object

    Returns: Python dictionary json-like object.
    '''
    return json.dumps(json_string)
