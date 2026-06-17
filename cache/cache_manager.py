import json
import sqlite3
import time
from pathlib import Path

CACHE_DB = Path(".cache/osint_cache.db")

CACHE_TTL = 24 * 60 * 60


class CacheManager:

    def __init__(self):

        CACHE_DB.parent.mkdir(
            exist_ok=True
        )

        self.conn = sqlite3.connect(
            CACHE_DB
        )

        self.create_table()

    def create_table(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cache (
                query TEXT PRIMARY KEY,
                data TEXT NOT NULL,
                created_at INTEGER NOT NULL
            )
            """
        )

        self.conn.commit()

    def get(self, query: str):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT data, created_at
            FROM cache
            WHERE query = ?
            """,
            (query,)
        )

        row = cursor.fetchone()

        if not row:
            return None

        data, created_at = row

        if time.time() - created_at > CACHE_TTL:

            self.delete(query)

            return None

        return json.loads(data)

    def set(self, query: str, report: dict):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO cache
            (
                query,
                data,
                created_at
            )
            VALUES (?, ?, ?)
            """,
            (
                query,
                json.dumps(report),
                int(time.time())
            )
        )

        self.conn.commit()

    def delete(self, query: str):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            DELETE FROM cache
            WHERE query = ?
            """,
            (query,)
        )

        self.conn.commit()

    def cleanup(self):

        cursor = self.conn.cursor()

        cutoff = int(
            time.time() - CACHE_TTL
        )

        cursor.execute(
            """
            DELETE FROM cache
            WHERE created_at < ?
            """,
            (cutoff,)
        )

        deleted = cursor.rowcount

        self.conn.commit()

        return deleted

    def count_entries(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM cache
            """
        )

        result = cursor.fetchone()

        return result[0]

    def database_size(self):

        if CACHE_DB.exists():

            return round(
                CACHE_DB.stat().st_size / 1024,
                2
            )

        return 0
