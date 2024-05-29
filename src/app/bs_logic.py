"""Module that contains all the bussiness logic"""
import os
from typing import Optional
from src.app import database
from datetime import datetime
# insert acquisition
def insert_acquisition(acq: dict) -> dict:
    """Insert a new acquisition in the database

    Args:
        acq (dict): dict following the acquisiton schema

    Returns:
        dict: _description_
    """
    insert_result = database.insert_db(os.getenv("ACQUIS_TABLE"),
                                        data=acq)
    if insert_result.get("insert_rows") == 1:
        msg = "El elemento fue insertado exitosamente."
    else:
        msg = "Hubo un error ingresando el elemento. " + insert_result.get("result") 

    acq["id"] = insert_result.get("inserted_id", 0)
    record_ins_result = insert_record("Create", acq)
    if record_ins_result.get("status_code") != 200:
        return {"content": record_ins_result.get("result"),
                "status_code": record_ins_result.get("status_code")}
    resp = {"content": msg,
            "status_code": insert_result.get("status_code")}
    return resp


# update acquisition
def update_acquisition(id: int, acq: dict) -> dict:
    """Module to update the adquisitions based on id

    Args:
        id (int): unique id 
        acq (dict): fields to update

    Returns:
        dict: response
    """
    upd_result = database.update_db(table_name=os.getenv("ACQUIS_TABLE"),
                                    object_id=id,
                                    update_criteria=acq)
    try:
        acq['id'] = id
        insert_record("update", acq)
    except Exception as e:
        msg = "Se actualizó el elemento pero hubo un error ingresando al historial: " + e.__str__()
        return {"content": msg,
                "status_code": 500}
    
    resp = {"content": upd_result.get("result"),
            "status_code": upd_result.get("status_code")}
    return resp


# search acquisitions
def search_acquisitions(search_criteria: dict) -> dict:
    new_search = {k:v for (k,v) in search_criteria.items() if v}
    search_result = database.search_db(table_name=os.getenv("ACQUIS_TABLE"),
                              criteria=new_search)
    resp = {"content": search_result.get("result"),
            "status_code": 200}
    return resp


# insert record
def insert_record(action: str, record: dict) -> dict:
    date = datetime.now().isoformat()
    data = {"id": None,
            "update_details": str(record),
            "action": action,
            "date": date}

    insert_result = database.insert_db(os.getenv("RECORDS_TABLE"),
                                        data=data)

    return insert_result
        

# search records
def search_record(date: Optional[str] = None) -> dict:
    if date:
        search_criteria = {"date": date}
    else:
        search_criteria={}
    search_result = database.search_db(table_name=os.getenv("RECORDS_TABLE"),
                              criteria=search_criteria)
    resp = {"content": search_result.get("result"),
            "status_code": search_result.get("status_code")}
    return resp

