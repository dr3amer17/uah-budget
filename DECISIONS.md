Chose the NBU API over ECB-backed ones like Frankfurter, because ECB doesn't carry UAH at all.
Chose NUMERIC over FLOAT for the rate, because floating point is approximate and money can't be.
Put the duplicate-prevention rule in the database as a UNIQUE constraint rather than in Python, because a constraint can't be bypassed by a buggy script.
Spent an hour on GitHub not loading - turned out to be QUIC/HTTP3 hanging on UDP, diagnosed by noticing curl succeeded over HTTP/1.1 while three browsers hung.
Twice ran commands that silently did nothing because the file wasn't saved - learned that no output doesn't mean success.
Kept the database URL in an environment variable rather than hardcoded, because the code has to run unchanged against a local Docker Postgres and a hosted one on deploy — only the environment differs.
Used ON CONFLICT DO NOTHING instead of letting the insert crash on a duplicate. The script will eventually run unattended on a schedule, and "already stored" isn't a failure — if it errors on every re-run, real failures get lost in the noise. This makes the script idempotent.
Check the response status code before calling .json(). Found this the hard way: request 24 of a 90-day backfill returned something that wasn't JSON and the parse crashed the entire run. Now a non-200 returns early, and the loop wraps each call in try/except so one bad day doesn't kill the rest.
Raised the delay between requests from 0.2s to 1s after what looked like throttling. NBU's API is free and public which is okay I can wait.