import os
from datetime import datetime

import httpx
import psycopg
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DATABASE_URL")


response = httpx.get(
    "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=GBP&json"
)
all_data = response.json()
data = all_data[0]

id_of = data["r030"]
currency_code = data["cc"]
rate = data["rate"]
date_string = data["exchangedate"]
rate_date = datetime.strptime(date_string, "%d.%m.%Y").date()

# print(currency_code, rate, rate_date)


with psycopg.connect(db_url) as conn:
    conn.execute(
        "INSERT INTO fx_rates (currency_code, rate, days_date) VALUES (%s, %s, %s)",
        (currency_code, rate, rate_date),
    )
