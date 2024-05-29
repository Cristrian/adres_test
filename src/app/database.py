""" Module for all the database operations"""
import os
import sqlite3
from typing import Union
# connect database
def db_con(db_name):
    con = sqlite3.connect(db_name)
    return con

def dict_factory(cursor, row):
    # Factory to get the results with its collumn
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

# execute statement
def exec_statement(con: sqlite3.Connection, stm: str, params: Union[dict, tuple]):
    # Creates cursor and execute it
    if "SELECT" in stm:
        # We set a row factory to get the response with column names
        con.row_factory = dict_factory
    cursor = con.cursor()
    exec_result = cursor.execute(stm, params)
    insert_rows = exec_result.rowcount
    inserted_id = exec_result.lastrowid
    result = exec_result.fetchall()
    con.commit()
    con.close()
    resp = {"result": result,
            "insert_rows": insert_rows,
            "status_code": 200,
            "inserted_id": inserted_id}
    return resp


# insert data, generates the sql statement
def insert_db(table_name:str, data: dict) -> dict:
    """Generates the statement to insert the data
    and inserts it

    Args:
        table_name (str): name of the table
        data (dict): data payload

    Returns:
        dict: response with result
    """
    values, data_tuple = generate_values_fields(data)
    stm = f"INSERT INTO {table_name} Values{values}"
    con = db_con(os.getenv("DATABASE"))
    try:
        result = exec_statement(
            con=con,
            stm=stm,
            params=data_tuple
        )
    except Exception as e:
        result = {"result": e.__str__(),
                  "insert_rows": 0,
                  "status_code": 500}
        con.close()
    
    return result


# Search data
def search_db(table_name:str, criteria: dict):
    stm = f"SELECT * FROM {table_name}"
    params = ()
    for i, key in enumerate(criteria):
        if i == 0:
            stm = stm + f" WHERE {key} = ?"
        else:
            stm = stm + f" AND {key} = ?"
        params = params +(criteria.get(key), )
    
    try:
        con = db_con(os.getenv("DATABASE"))
        result = exec_statement(
            con=con,
            stm=stm,
            params=params
        )
    except Exception as e:
        result = {"result": "Error buscando:" + e.__str__(),
                  "status_code": 500}
        con.close()
        
    return result


def update_db(table_name: str,object_id: int, update_criteria: dict):
    
    stm = f"UPDATE {table_name} SET "
    params = ()
    # Snippet that creates the update statement
    for i, collumn in enumerate(update_criteria):
        new_value = update_criteria.get(collumn)
        if i == len(update_criteria) - 1 :
            stm = stm + f"{collumn} = ? "
        else:
            stm = stm + f"{collumn} = ?,"
        params = params + (new_value,)
    try:
        con = db_con(os.getenv("DATABASE"))
        result = exec_statement(
            con=con,
            stm=stm,
            params=params
        )
        result["result"] = "El elemento se ha actualizado correctamente"
    except Exception as e:
        result = {"result": e.__str__(),
                  "status_code": 500}
        con.close()
    
    return result


def generate_values_fields(data: dict) -> str:
    """Generates values fields string for insert statement
    for example:
    (:id, :name, :type, :date)
    Args:
        data (_type_): _description_
    Returns:
        str: string with values
    """
    table_fields = ""
    data_tuple = ()
    for i, key in enumerate(data.keys()):
        if i == 0:
            table_fields = table_fields + "(:" + key
        elif i == data.keys().__len__() - 1 :
            table_fields = table_fields + f",:{key})"
        else:
            table_fields = table_fields + ",:" + key
        data_tuple = data_tuple + (data.get(key),)
    return table_fields, data_tuple

