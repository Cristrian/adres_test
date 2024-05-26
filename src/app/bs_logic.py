import os
from app import database
# insert acquisition
def insert_acquisition(acq: dict) -> dict:
    try:
        acq["id"] = None
        insert_result = database.insert_db(os.getenv("ACQUIS_TABLE"),
                                           data=acq)
        if insert_result.get("insert_rows") == 1:
            msg = "El elemento fue insertado exitosamente."
        else:
            msg = "Hubo un error ingresando el elemento."
            
        #TODO Historial de creación de elemento
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
    search_result = database.search_db(table_name=os.getenv("ACQUIS_TABLE"),
                              criteria=search_criteria)
    resp = {"content": search_result,
            "status_code": 200}
    return resp

# insert record
def insert_record(record: dict) -> dict:
    return

# search records
def search_record(search_criteria: dict) -> dict:
    return
