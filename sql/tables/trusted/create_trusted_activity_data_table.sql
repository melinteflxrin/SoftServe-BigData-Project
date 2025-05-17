CREATE TABLE IF NOT EXISTS trusted.activity_data (
    activity_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK (age > 0),
    gender VARCHAR(50) NOT NULL CHECK (gender IN ('male', 'female', 'other')),
    timestamp TIMESTAMP NOT NULL,
    activity_type VARCHAR(100) NOT NULL,
    steps INT NOT NULL CHECK (steps >= 0),
    heart_rate INT NOT NULL CHECK (heart_rate >= 0),
    calories_burned INT NOT NULL CHECK (calories_burned >= 0)
);