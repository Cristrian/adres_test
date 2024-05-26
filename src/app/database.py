import sqlite3
# connect database
def db_con(db_name):
    con = sqlite3.connect(db_name)
    return con

# execute statement
def exec_statement(con: sqlite3.Connection, stm: str, params: tuple):
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
def insert_db(table_fields: str, data: tuple):
    
    return