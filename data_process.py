import pyodbc
import json
from datetime import datetime

def datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()

def accdb_to_json(db_path, table_name, json_file_name):
    conn = None
    try:
        conn_str = (
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=" + db_path + ";"
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Define the SQL query to select specific columns where INCIDENT_YEAR > 2015
        sql_query = f"""
        SELECT 
            INCIDENT_MONTH, INCIDENT_YEAR, TIME_OF_DAY, REMAINS_COLLECTED, AIRPORT, STATE, HEIGHT, SPEED, SPECIES
        FROM 
            {table_name}
        WHERE gi
            INCIDENT_YEAR > 2015
        """
        
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        
        columns = [column[0] for column in cursor.description]
      
        data_dicts = [dict(zip(columns, row)) for row in rows]
        
        json_data = json.dumps(data_dicts, indent=4, default=datetime_converter)
        
        with open(json_file_name, 'w') as json_file:
            json_file.write(json_data)
        
        print(f"Filtered data has been successfully converted to JSON and saved as {json_file_name}.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if conn is not None:
            conn.close()

db_path = r"C:\Users\eli18\OneDrive\Desktop\research\ACRP-Graduate-Research-data-exploration\Public.accdb"

accdb_to_json(db_path, 'STRIKE_REPORTS', 'filtered_output.json')
