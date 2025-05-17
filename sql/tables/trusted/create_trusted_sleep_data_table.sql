CREATE TABLE IF NOT EXISTS trusted.sleep_data (
    sleep_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES trusted.user_profile(user_id),
    date DATE NOT NULL,
    sleep_start TIMESTAMP NOT NULL,
    sleep_end TIMESTAMP NOT NULL,
    sleep_duration_hours DECIMAL(5,1) NOT NULL CHECK (sleep_duration_hours > 0),
    sleep_quality_score INT NOT NULL CHECK (sleep_quality_score BETWEEN 0 AND 100)
);