CREATE TABLE raw.activity_log (
    activity_id      SERIAL PRIMARY KEY,
    user_id          INTEGER,
    timestamp        TIMESTAMP,
    activity_type    VARCHAR(50),
    steps            INTEGER,
    heart_rate       INTEGER,
    calories_burned  INTEGER
);