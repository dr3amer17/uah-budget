Chose the NBU API over ECB-backed ones like Frankfurter, because ECB doesn't carry UAH at all.
Chose NUMERIC over FLOAT for the rate, because floating point is approximate and money can't be.
Put the duplicate-prevention rule in the database as a UNIQUE constraint rather than in Python, because a constraint can't be bypassed by a buggy script.
Spent an hour on GitHub not loading - turned out to be QUIC/HTTP3 hanging on UDP, diagnosed by noticing curl succeeded over HTTP/1.1 while three browsers hung.
Twice ran commands that silently did nothing because the file wasn't saved - learned that no output doesn't mean success.