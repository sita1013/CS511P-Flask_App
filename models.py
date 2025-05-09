import sqlite3

DB_PATH = 'scottish_stats.db'

def get_filtered_deployments():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''
        SELECT d.date_code, d.measurement, d.units, d.value, s.name AS industry_name
        FROM deployments d
        JOIN sectors s ON d.sector_code = s.code
        ''')
    rows = cur.fetchall()
    conn.close()
    return rows