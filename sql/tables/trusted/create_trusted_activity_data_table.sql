CREATE TABLE IF NOT EXISTS trusted.activity_data (
    activity_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255),
    age INT,
    gender VARCHAR(50),
    timestamp TIMESTAMP NOT NULL,
    activity_type VARCHAR(100),
    steps INT,
    heart_rate INT,
    calories_burned INT
);