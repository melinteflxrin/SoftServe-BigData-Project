CREATE TABLE IF NOT EXISTS trusted.goals_data (
    goal_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK (age > 0),
    gender VARCHAR(50) NOT NULL CHECK (gender IN ('male', 'female', 'other')),
    date DATE NOT NULL,
    goal_type VARCHAR(100) NOT NULL,
    target_value INT NOT NULL CHECK (target_value >= 0),
    actual_value INT CHECK (actual_value >= 0),
    status VARCHAR(50) NOT NULL CHECK (status IN ('ACHIEVED', 'NOT ACHIEVED', 'PENDING'))
);