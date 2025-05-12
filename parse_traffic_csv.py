import csv
import sqlite3

DB_NAME = 'traffic_stats.db'
def parse_csv():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS indicators')
    print("table re-dropped successfully");
    cur.execute('DROP TABLE IF EXISTS traffic_stats')
    print("table re-created successfully");
    cur.execute('''
        CREATE TABLE indicators (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT UNIQUE
        )
    ''')
    cur.execute('''
        CREATE TABLE traffic_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            feature_name TEXT,
            feature_type TEXT,
            date_code INTEGER, 
            measurement TEXT,
            units TEXT, 
            value REAL,
            indicator_id INTEGER,
            FOREIGN KEY (indicator_id) REFERENCES indicators(id) 
        )
    ''')

    with open('traffic_stats.csv', newline='') as f:
        reader = csv.DictReader(f)
        indicator_cache = {}
        for row in reader:
            feature_name = (row['FeatureName'])
            feature_type = (row['FeatureType'])
            date_code = int(row['DateCode'])
            measurement = (row['Measurement'])
            units = (row['Units'])
            value = float(row['Value']) if row['Value'] else None
            indicator_name = (row['Indicator (road network traffic)'])
            try: 
                if not feature_name or not feature_type: 
                    continue
                if indicator_name not in indicator_cache: 
                    cur.execute(
                        'INSERT OR IGNORE INTO indicators (name) VALUES (?)',
                        (indicator_name,)
                    )
                    conn.commit()
                    cur.execute('SELECT id FROM indicators WHERE name = ?', (indicator_name,))
                    indicator_cache[indicator_name] = cur.fetchone()[0]

                indicator_id = indicator_cache[indicator_name]
                cur.execute('''
                    INSERT INTO traffic_stats (feature_name, feature_type, date_code, measurement, units, value, indicator_id)
                    VALUES (?,?,?,?,?,?,?)
                ''', (feature_name, feature_type, date_code, measurement, units, value, indicator_id))  
            except: 
                print("There was an issue with parsing the data")
    conn.commit()
    conn.close()
    print("CSV parsed and loaded into traffic_stats.db")