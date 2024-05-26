import os
import sqlite3
from dotenv import load_dotenv

load_dotenv(override=True)

if __name__ == "__main__":
    datab = os.getenv("DATABASE")
    con = sqlite3.Connection(database=datab)
    cursor = con.cursor()
    
    acq_table = os.getenv("ACQUIS_TABLE","acquisitions")
    record_table = os.getenv("RECORDS_TABLE","records")
    
    stm_acq = (f"CREATE TABLE {acq_table}" 
           "(id integer primary key autoincrement, "
           "budget real,"
           "unit text,"
           "acq_type text,"
           "quantity integer,"
           "cost_per_unit real,"
           "total_value real,"
           "adquisition_date text,"
           "supplier text,"
           "documentation text)"
           )
    cursor.execute(stm_acq)
    
    stm_record=(f"CREATE TABLE {record_table}" 
           "(id integer primary key autoincrement, "
           "update_details text,"
           "record_date text)")
    con.commit()
    con.close()