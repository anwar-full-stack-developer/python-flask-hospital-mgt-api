import sqlite3
from db_connection import create_db_table, get_db_connection

# connection = sqlite3.connect('database.db')
connection = get_db_connection()

# create user table
# create_db_table()

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


def create_tables():
    tables = [
        """DROP TABLE IF EXISTS games;
        CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
				price REAL NOT NULL,
				rate INTEGER NOT NULL
            )
            """
    ]
    cursor = cur
    for table in tables:
        cursor.execute(table)
    
create_tables()


cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
            ('admin', 'admin@admin.com', '42423424', "NY, USA", "USA")
            )
cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
            ('test', 'test@test.com', '42423424', "NY, USA", "USA")
            )

connection.commit()
connection.close()