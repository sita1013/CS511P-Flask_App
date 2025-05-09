import csv
import sqlite3

DB_NAME = 'scottish_stats.db'
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS deployments')
print("table dropped successfully");
cur.execute('DROP TABLE IF EXISTS sectors')
print("table created successfully");
cur.execute('''
    CREATE TABLE sectors (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        code TEXT UNIQUE, 
        name TEXT
    )
''')
cur.execute('''
    CREATE TABLE deployments (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        date_code INTEGER, 
        measurement TEXT,
        units TEXT, 
        value REAL,
        sector_code TEXT,
        FOREIGN KEY (sector_code) REFERENCES sectors(code) 
    )
''')

with open('scottish_stats.csv', newline='') as f:
    reader = csv.DictReader(f)
    sectors_seen = set()
    for row in reader:
        date = int(row['DateCode'])
        measurement = (row['Measurement'])
        units = (row['Units'])
        value = float(row['Value']) if row['Value'] else None
        sector_code = row['Industry Sector (SIC 07)']
        sector_name = row['Industry Type']
        if not sector_code or not sector_name: 
            continue
        if sector_code not in sectors_seen: 
            cur.execute(
                'INSERT OR IGNORE INTO sectors (code, name) VALUES (?, ?)',
                (sector_code, sector_name)
            )
            sectors_seen.add(sector_code)
        cur.execute('''
                INSERT INTO deployments (date_code, measurement, units, value, sector_code)
                VALUES (?,?,?,?,?)
                ''', 
                (date, measurement, units, value, sector_code))  
conn.commit()
conn.close()
print("data parsed successfully")