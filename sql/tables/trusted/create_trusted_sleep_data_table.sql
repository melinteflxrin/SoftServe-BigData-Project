CREATE TABLE IF NOT EXISTS trusted.sleep_data (
    sleep_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255),
    age INT,
    gender VARCHAR(50),
    date DATE NOT NULL,
    sleep_start TIMESTAMP NOT NULL,
    sleep_end TIMESTAMP NOT NULL,
    sleep_duration_hours DECIMAL(5,1),
    sleep_quality_score INT
);