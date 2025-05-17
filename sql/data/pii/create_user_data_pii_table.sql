CREATE TABLE IF NOT EXISTS trusted.user_data_pii (
    user_id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT CHECK (age > 0),
    gender VARCHAR(50) CHECK (gender IN ('male', 'female', 'other'))
);