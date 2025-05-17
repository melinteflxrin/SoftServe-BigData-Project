CREATE TABLE IF NOT EXISTS trusted.activity_data (
    activity_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES trusted.user_profile(user_id),
    timestamp TIMESTAMP NOT NULL,
    activity_type VARCHAR(100) NOT NULL,
    steps INT NOT NULL CHECK (steps >= 0),
    heart_rate INT NOT NULL CHECK (heart_rate >= 0),
    calories_burned INT NOT NULL CHECK (calories_burned >= 0)
);