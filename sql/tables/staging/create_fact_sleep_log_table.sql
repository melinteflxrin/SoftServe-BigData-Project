CREATE TABLE IF NOT EXISTS staging.fact_sleep_log (
    sleep_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    date DATE NOT NULL,
    sleep_start TIMESTAMP NOT NULL,
    sleep_end TIMESTAMP NOT NULL,
    sleep_duration_hours DECIMAL(5, 1),
    sleep_quality_score INT
);