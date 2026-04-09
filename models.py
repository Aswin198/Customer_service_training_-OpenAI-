import sqlite3

def get_db_connection():
    conn = sqlite3.connect("simulator.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scenario_id INTEGER,
            scenario_title TEXT,
            user_response TEXT,
            overall_score REAL,
            strengths TEXT,
            improvements TEXT,
            suggested_reply TEXT
        )
    """)

    conn.commit()
    conn.close()