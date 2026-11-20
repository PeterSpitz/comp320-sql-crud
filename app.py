import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("users.db", isolation_level=None)

# Create the users table if it doesn’t exist
with conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)
print("Table created successfully!")