import unittest
import sqlite3
import os
from parse_csv import DB_NAME
import parse_csv

class TestCSVParsing(unittest.TestCase):
    def setUp(self):
        parse_csv

    def test_deployments_table_exists(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='deployments'")
        table = cur.fetchone()
        self.assertIsNotNone(table, "deployments table should exist")
        conn.close()

    def test_data_inserted(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM deployments")
        count = cur.fetchone()[0]
        self.assertGreater(count, 0, "deployments table should have at least one row")
        conn.close()

    def test_sector_linked(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            SELECT d.sector_code
            FROM deployments d
            LEFT JOIN sectors s ON d.sector_code = s.code
            WHERE s.id IS NULL
        """)
        broken_links = cur.fetchall()
        self.assertEqual(len(broken_links), 0, "All deployments should be linked to a valid sector")
        conn.close()

if __name__ == '__main__':
    unittest.main()