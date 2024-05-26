import os
import sqlite3
from typing import Union
# connect database
def db_con(db_name):
    con = sqlite3.connect(db_name)
    return con

# execute statement
def exec_statement(con: sqlite3.Connection, stm: str, params: Union[dict, tuple]):
    # Creates cursor and execute it
    cursor = con.cursor()
    exec_result = cursor.execute(stm, params)
    total_rows = exec_result.rowcount
    result = exec_result.fetchall()
    con.commit()
    con.close()
    resp = {"result": result,
            "total_rows": total_rows}
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
    values = generate_values_fields(data)
    stm = f"INSERT INTO {table_name} Values{values}"
    result = exec_statement(
        con=db_con(os.getenv("DATABASE")),
        stm=stm,
        params=data
    )
    
    return result


# Search data
def search_db(table_name:str, criteria: dict):
    stm = f"SELECT * FROM {table_name}"
    result = exec_statement(
        con=db_con(os.getenv("DATABASE")),
        stm=stm,
        params=()
    )
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
    for i, key in enumerate(data.keys()):
        if i == 0:
            table_fields = table_fields + "(:" + key
        elif i == data.keys().__len__() - 1 :
            table_fields = table_fields + f",:{key})"
        else:
            table_fields = table_fields + ",:" + key
    return table_fields