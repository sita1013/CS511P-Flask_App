import sqlite3

DB_PATH = 'scottish_stats.db'

def get_filtered_deployments():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM deployments")
    rows = cur.fetchall()
    conn.close()
    return rows