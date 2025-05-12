import unittest
import sqlite3
from parse_traffic_csv import DB_NAME, parse_csv

class TestTrafficCSVParsing(unittest.TestCase):
    def setUp(self):
        parse_csv()

    def test_traffic_stats_table_exists(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='traffic_stats'")
        table = cur.fetchone()
        self.assertIsNotNone(table, "traffic_stats table should exist")
        conn.close()

    def test_data_inserted(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM traffic_stats")
        count = cur.fetchone()[0]
        self.assertGreater(count, 0, "traffic_stats table should have at least one row")
        conn.close()

    def test_indicator_linked(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            SELECT t.indicator_id
            FROM traffic_stats t
            LEFT JOIN indicators i ON t.indicator_id = i.id
            WHERE i.id IS NULL
        """)
        broken_links = cur.fetchall()
        self.assertEqual(len(broken_links), 0, "All traffic_stats should be linked to a valid indicator")
        conn.close()

if __name__ == '__main__':
    unittest.main()