CREATE TABLE fx_rates (
    id SERIAL PRIMARY KEY,
    currency_code TEXT NOT NULL,
    rate NUMERIC(10, 4) NOT NULL,
    days_date date NOT NULL,
    fetched_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    UNIQUE(currency_code, days_date)
)

