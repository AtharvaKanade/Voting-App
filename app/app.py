import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        database=os.environ.get("DB_NAME", "votingdb"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "password")
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id SERIAL PRIMARY KEY,
            vote VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT vote, COUNT(*) FROM votes GROUP BY vote")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    results = {"Cats": 0, "Dogs": 0}
    for row in rows:
        if row[0] in results:
            results[row[0]] = row[1]

    total = sum(results.values())
    return render_template("index.html", results=results, total=total)

@app.route("/vote", methods=["POST"])
def vote():
    choice = request.form.get("vote")
    if choice in ["Cats", "Dogs"]:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO votes (vote) VALUES (%s)", (choice,))
        conn.commit()
        cur.close()
        conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)

