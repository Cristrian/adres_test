import os
import database
# insert acquisition
def insert_acquisition(acq: dict) -> dict:
    try:
        insert_result = database.insert_db(os.getenv("ACQUIS_TABLE"),
                                           data=acq)
        if insert_result.get("total_rows") == 1:
            msg = "El elemento fue insertado exitosamente."
        else:
            msg = "Hubo un error ingresando el elemento."
        resp = {"content": msg,
                "status_code": 200}
    except Exception as e:
        msg = "Error ingresando datos a la base de datos: " + e.__str__()
        resp = {"content": msg,
                "status_code": 500}
    return resp

# update acquisition
def update_acquisition(acq: dict) -> dict:
    return

# search acquisitions
def search_acquisitions(search_criteria: dict) -> dict:
    resp = database.search_db(table_name=os.getenv("ACQUIS_TABLE"),
                              criteria=search_criteria)
    return resp

# insert record
def insert_record(record: dict) -> dict:
    return

# search records
def search_record(search_criteria: dict) -> dict:
    return
