#   Project INFO


# UAH Budget

A budgeting tool for people living in the UK who spend money from Ukrainian bank accounts.

## The problem

Since the war in Ukraine began, the UK has accepted refugees and made it possible for Ukrainians to live, work and study here. But many of us, myself included, still use Ukrainian banks and cards to pay for groceries and day-to-day things.

That creates a budgeting problem. My money arrives monthly in UAH, and there is a national limit on how much can be spent abroad from a Ukrainian bank - 100,000 UAH per month, about 1,800 GDP. Every price I see is in pounds, but every payment leaves my account is in hryvnia at whatever the exchange rate happens to be that day and time.

Existing budgeting apps assume you earn and spend in one currency. This one doesn't.

## Who it's for

Ukrainians living in the UK who hold money in UAH and spend it in GBP. Initially me, then anyone in the same situation.

## What it does (v1)

- Converts your UAH balance to GBP using the current exchange rate
- Tells you how much you can spend per week to make the balance last the month
- Shows exchange rate history, so you can see how much your money has gained or lost value over time
- Warns you as you approach the 100,000 UAH monthly spending limit

The weekly figure is the point of the app. Anyone can look up a conversion rate; the useful question is "how much can I actually spend this week?"

## Not doing

Deliberately out of scope for v1:

- Bank card integration - no automatic transaction sync
- Currencies other than UAH and GBP
- Mobile app
- Multiple user accounts and logins
- Spending categories and receipt tracking

## Stack

- **Python / FastAPI** - my strongest language; FastAPI turns the conversion logic into an API the frontend can call
- **PostgreSQL** - stores exchange rate history as time-series data
- **React** - frontend
- **Docker** - runs Postgres locally, so the setup is identical on any machine

Exchange rates come from the National Bank of Ukraine's open API, which is the authoritative source for UAH. ECB-backed APIs don't carry hryvnia.

## Status

In progress. Started August 2026.

**10/08/2026** - Environment set up: Docker, PostgreSQL, Python virtual environment, Git repository.

**11/08/2026** - Defined project scope and wrote README. Confirmed the NBU API response format.

**18/08/2026** - Created a schema and DECISIONS file to keep track of everything.

**19/08/2026** -  Created fx_rates table. Wrote the fetch script: calls the NBU API, parses the response, and inserts a rate into PostgreSQL.

**20/08/2026** - Ingestion pipeline complete. Backfilled 91 days of GBP/UAH rate history with error handling and rate limiting.



{"r030":826,"txt":"фунт стерлінгів","rate":60.5167,"cc":"GBP","exchangedate":"11.08.2026"}