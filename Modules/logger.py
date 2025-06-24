import os
import sqlite3
from datetime import datetime

class QueryLog:
    def __init__(self, db_path='querry_log.db'):
        self.db_path = db_path
        self.conn = None

    def _create_table(self):
        '''
        This function creates a table for logging the query with answer with sources and timestamps.
        '''
        if not os.path.exists(os.path.join(os.getcwd(), self.db_path)):
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS queries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME,
                    query TEXT,
                    answer TEXT,
                    sources TEXT
                )
            ''')
            self.conn.commit()

    def log_query(self, query, answer, sources):
        '''
        This function logs the necessary data
        '''

        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

        timestamp = datetime.now().isoformat()
        sources_str = ",".join(sources)
        self.conn.execute(
            "INSERT INTO queries (timestamp, query, answer, sources) VALUES (?, ?, ?, ?)",
            (timestamp, query, answer, sources_str)
        )
        self.conn.commit()
        self.conn.close()