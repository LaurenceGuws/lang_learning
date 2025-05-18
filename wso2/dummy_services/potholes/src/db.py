import sqlite3
import os
from pathlib import Path
from contextlib import contextmanager

# Get the absolute path to the database file
DB_PATH = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) / "db" / "pothole.db"

@contextmanager
def get_db_connection():
    """Context manager for database connections."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def execute_query(query, params=None):
    """Execute a query and return all results."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor.fetchall()

def execute_insert(query, params=None):
    """Execute an insert and return the last row id."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor.lastrowid

def get_by_id(table, id):
    """Get a record by id from the specified table."""
    query = f"SELECT * FROM {table} WHERE id = ?"
    results = execute_query(query, (id,))
    return results[0] if results else None 