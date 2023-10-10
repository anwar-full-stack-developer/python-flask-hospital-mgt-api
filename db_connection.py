import sqlite3

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    try:
        conn = get_db_connection()
        conn.execute('''
            DROP TABLE IF EXISTS users;
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("User table created successfully")
    except:
        print("User table creation failed - Maybe table")
    finally:
        conn.close()