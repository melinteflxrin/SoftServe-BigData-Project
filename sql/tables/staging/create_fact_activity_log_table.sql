CREATE TABLE IF NOT EXISTS staging.fact_activity_log (
    activity_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    activity_type VARCHAR(100),
    steps INT,
    heart_rate INT,
    calories_burned INT
);