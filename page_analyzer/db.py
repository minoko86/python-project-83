from datetime import date
import os
from psycopg2 import extras
import psycopg2
from dotenv import load_dotenv

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)
load_dotenv()


class DB:
    def get_url_by_id(self, id):
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                cursor.execute("""
                            SELECT
                                id,
                                name,
                                created_at
                            FROM
                                urls
                            WHERE
                                id = %s;
                            """, (id,))
                return cursor.fetchone()


    def get_checks_by_url_id(self, id):
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                cursor.execute("""
                            SELECT
                                id,
                                url_id,
                                status_code,
                                h1,
                                title,
                                description,
                                created_at
                            FROM
                                url_checks
                            WHERE
                                url_id = %s;
                            """, (id,))
                return cursor.fetchall()


    def get_url_by_name(self, name):
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                cursor.execute("""
                            SELECT
                                id,
                                name,
                                created_at
                            FROM
                                urls
                            WHERE
                                name = %s;
                            """, (name,))
                return cursor.fetchone()


    def get_all_urls(self):
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                cursor.execute("""
                            SELECT
                                id,
                                name,
                                created_at
                            FROM
                              urls
                            ORDER BY
                              id DESC;
                            """)
                return cursor.fetchall()


    def get_last_url_checks(self):
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                cursor.execute("""
                            SELECT
                                DISTINCT ON (url_id)
                                id,
                                url_id,
                                status_code,
                                h1,
                                title,
                                description,
                                created_at
                            FROM
                              url_checks
                            ORDER BY
                              url_id, created_at DESC;
                            """)
                return cursor.fetchall()


    def create_url(self, name):
        creation_date = date.today()
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                cursor.execute("""
                            INSERT INTO urls (name, created_at)
                            VALUES
                              (%s, %s) RETURNING id;
                            """, (name, creation_date))
                return cursor.fetchone()[0]


    def create_check(self, id, code, h1, title, description):
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                creation_date = date.today()
                cursor.execute("""
                            INSERT INTO url_checks (
                              url_id, status_code, h1, title, description,
                              created_at
                            )
                            VALUES
                              (%s, %s, %s, %s, %s, %s);
                            """, (id, code, h1, title, description, creation_date))


    def get_check_by_url_id(self, id):
        with conn:
            with conn.cursor(cursor_factory=extras.NamedTupleCursor) as cursor:
                cursor.execute("""
                            SELECT
                              id,
                              url_id,
                              status_code,
                              h1,
                              title,
                              description,
                              created_at
                            FROM
                              url_checks
                            WHERE
                              url_id = %s;
                            """, (id,))
                return cursor.fetchall()
