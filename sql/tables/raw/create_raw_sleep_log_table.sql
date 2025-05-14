CREATE TABLE IF NOT EXISTS raw.sleep_log (
    sleep_id            SERIAL PRIMARY KEY,
    user_id             INTEGER,
    date                DATE,
    sleep_start         TIMESTAMP,
    sleep_end           TIMESTAMP,
    sleep_quality_score INTEGER
);