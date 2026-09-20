import os

import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
db_url = os.getenv("DATABASE_URL")

app = FastAPI()


def get_latest_rate_from_db():
    with psycopg.connect(db_url) as conn:
        return conn.execute(
            "SELECT currency_code, rate, days_date FROM fx_rates ORDER BY days_date DESC LIMIT 1"
        ).fetchone()


@app.get("/rates/latest")
def get_latest_rate():
    row = get_latest_rate_from_db()
    return {"currency_code": row[0], "rate": float(row[1]), "date": row[2]}


@app.get("/convert")
def convert(uah: float):
    row = get_latest_rate_from_db()
    rate = float(row[1])
    gbp = uah / rate

    return {"uah": uah, "rate": rate, "gbp": round(gbp, 2)}