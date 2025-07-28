import sqlite3
import pandas as pd

def execute_sql_query(query):
    conn = sqlite3.connect("database.db")
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return pd.DataFrame({"error": [str(e)]})
    finally:
        conn.close()
