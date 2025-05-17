CREATE TABLE IF NOT EXISTS trusted.sleep_data (
    sleep_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK (age > 0),
    gender VARCHAR(50) NOT NULL CHECK (gender IN ('male', 'female', 'other')),
    date DATE NOT NULL,
    sleep_start TIMESTAMP NOT NULL,
    sleep_end TIMESTAMP NOT NULL,
    sleep_duration_hours DECIMAL(5,1) NOT NULL CHECK (sleep_duration_hours > 0),
    sleep_quality_score INT NOT NULL CHECK (sleep_quality_score BETWEEN 0 AND 100)
);