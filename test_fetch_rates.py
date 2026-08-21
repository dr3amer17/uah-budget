from datetime import date

from fetch_rates import parse_rate_response


def test_parses_valid_response():
    fake = [
        {
            "r030": 826,
            "txt": "Фунт стерлінгів",
            "rate": 60.5841,
            "cc": "GBP",
            "exchangedate": "20.08.2026",
        }
    ]

    result = parse_rate_response(fake)
    assert result["currency_code"] == "GBP"
    assert result["rate"] == 60.5841
    assert result["rate_date"] == date(2026, 8, 20)


def test_parses_day_first_dates():
    fake = [{"cc": "GBP", "rate": 60.0, "exchangedate": "01.02.2026"}]
    result = parse_rate_response(fake)
    assert result["rate_date"] == date(2026, 2, 1)


def test_empty_response_returns_none():
    assert parse_rate_response([]) is None
