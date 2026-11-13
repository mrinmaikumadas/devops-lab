from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        os.environ["DATABASE_URL"]
    )

@app.route("/init")
def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            ts TIMESTAMP DEFAULT NOW()
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "database initialized"

@app.route("/count")
def count():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO visits (ts) VALUES (NOW())"
    )

    cur.execute("SELECT COUNT(*) FROM visits")

    n = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(total_visits=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
