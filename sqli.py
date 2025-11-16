from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "demo.db"

# Create database + users table if missing
def init_db():
    needs_init = not os.path.exists(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    if needs_init:
        conn.executescript("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            );
        """)
    conn.close()

init_db()

@app.route("/")
def home():
    return """
    <h2>SQL Injection Demo (SQLite)</h2>
    <p>Add a user:</p>
    <code>/add?name=Alice</code><br><br>

    <p>Drop the table via SQL injection:</p>
    <code>/add?name=test'); DROP TABLE users; --</code><br><br>

    <p>View table:</p>
    <code>/show</code>
    """

@app.route("/add")
def add():
    name = request.args.get("name", "")

    # ❗ VULNERABLE: executescript() allows multiple statements
    sql = f"INSERT INTO users (name) VALUES ('{name}');"

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(sql)   # <-- This WILL run injected DROP TABLE
    conn.commit()
    conn.close()

    return "Executed."

@app.route("/show")
def show():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        return "<br>".join([str(r) for r in rows])
    except Exception as e:
        return f"<b>Error:</b> {e}"

if __name__ == "__main__":
    app.run(debug=True)

