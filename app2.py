import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db", isolation_level=None)

# Create the users table if it doesn't exist
with conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)

# Insert data without explicitly calling commit
#conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
#conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
#conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 35))
#conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 40))

conn.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")

conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))

conn.execute("INSERT INTO users (name, age) VALUES ('Bob', '30')")

conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", "30"))

conn.execute("DELETE FROM users")

# Fetch all users to check if the data was inserted
print("Users in the database:")
for row in conn.execute("SELECT * FROM users"):
    print(row)

# Close the connection
conn.close()
