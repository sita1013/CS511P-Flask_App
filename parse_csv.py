import csv
import sqlite3

    # open the connection to the database
conn = sqlite3.connect('polar_bear_data.db')
cur = conn.cursor()

    # drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS deployments')
print("table dropped successfully");
    # create table again
conn.execute('CREATE TABLE deployments (BearID INTEGER, PTT_ID INTEGER, capture_lat REAL, capture_long REAL, Sex TEXT, Age_class TEXT, Ear_applied TEXT)')
print("table created successfully");

    # open the file to read it into the database
with open('scottish_stats.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        Date = int(row[3])
        Measurement = (row[4])
        Units = (row[5])
        Value = float(row[6])
        Industry_Sector = row[7]

        cur.execute('INSERT INTO deployments VALUES (?,?,?,?,?)', (Date, Measurement, Units, Value, Industry_Sector))
    print("data parsed successfully");
    conn.commit()
    conn.close()