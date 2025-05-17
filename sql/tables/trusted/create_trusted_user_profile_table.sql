CREATE TABLE IF NOT EXISTS trusted.user_profile (
    user_id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK (age > 0),
    gender VARCHAR(50) NOT NULL CHECK (gender IN ('male', 'female', 'other'))
);