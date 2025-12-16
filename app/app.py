import os
import psycopg2
from flask import Flask

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "35.189.233.194")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_NAME = os.environ.get("DB_NAME", "myapp")       
DB_USER = os.environ.get("DB_USER", "myuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "STRONG_PASSWORD")

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

@app.route("/")
def hello():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT 'Hello la team avec PostgreSQL!'")
        result = cur.fetchone()[0]
        cur.close()
        conn.close()
        return result
    except Exception as e:
        return f"Erreur DB: {e}"
