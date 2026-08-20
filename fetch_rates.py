import os
import time
from datetime import date, datetime, timedelta

import httpx
import psycopg
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DATABASE_URL")


def fetch_and_store(target_date):

    print("Fetching: ", target_date)
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=GBP&date={target_date.strftime('%Y%m%d')}&json"
    response = httpx.get(url, timeout=30.0)
    if response.status_code != 200:
        print(f" Bad status {response.status_code} for {target_date}")
        return  # leaves function early as its not valid
    all_data = response.json()
    data = all_data[0]

    currency_code = data["cc"]
    rate = data["rate"]
    date_string = data["exchangedate"]
    rate_date = datetime.strptime(date_string, "%d.%m.%Y").date()

    # print(currency_code, rate, rate_date)

    with psycopg.connect(db_url) as conn:
        conn.execute(
            "INSERT INTO fx_rates (currency_code, rate, days_date) VALUES (%s, %s, %s) ON CONFLICT (currency_code, days_date) DO NOTHING",
            (currency_code, rate, rate_date),
        )

    time.sleep(1.0)

DAYS_TO_BACKFILL = 90
for i in range(DAYS_TO_BACKFILL):
    day = date.today() - timedelta(days=i)
    try:
        fetch_and_store(day)
    except httpx.HTTPError as e:
        print(f"Failed for {day}: {e}")
