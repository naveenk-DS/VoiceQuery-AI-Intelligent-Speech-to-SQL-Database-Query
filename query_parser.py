# query_parser.py

import sqlite3

def execute_sql_query(query, db_path="database.db"):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        return f"Error: {e}"
