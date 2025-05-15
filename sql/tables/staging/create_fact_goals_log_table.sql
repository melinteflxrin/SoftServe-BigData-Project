CREATE TABLE IF NOT EXISTS staging.fact_goals_log (
    goal_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    date DATE NOT NULL,
    goal_type VARCHAR(100),
    target_value INT,
    actual_value INT,
    status VARCHAR(50)
);