import sqlite3

DB_PATH = 'traffic_stats.db'

def get_years_and_features():
    conn = sqlite3.connect('traffic_stats.db')
    cur = conn.cursor()
    years = [row[0] for row in cur.execute('SELECT DISTINCT date_code FROM traffic_stats ORDER BY date_code')]
    features = [row[0] for row in cur.execute('SELECT DISTINCT feature_name FROM traffic_stats ORDER BY feature_name')]
    conn.close()
    return years, features

def get_filtered_data(year=None, feature=None):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    query = '''
        SELECT t.units, t.value, t.measurement, i.name AS indicator_name
        FROM traffic_stats t
        JOIN indicators i ON t.indicator_id = i.id
        WHERE 1=1
    '''
    params = []
    if year: 
        query += 'AND t.date_code = ?'
        params.append(year)
    if feature: 
        query += 'AND t.feature_name = ?'
        params.append(feature)
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows