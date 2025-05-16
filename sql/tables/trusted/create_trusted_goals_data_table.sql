CREATE TABLE IF NOT EXISTS trusted.goals_data (
    goal_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255),
    age INT,
    gender VARCHAR(50),
    date DATE NOT NULL,
    goal_type VARCHAR(100),
    target_value INT,
    actual_value INT,
    status VARCHAR(50)
);