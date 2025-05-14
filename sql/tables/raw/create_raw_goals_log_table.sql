CREATE TABLE IF NOT EXISTS raw.goals_log (
    goal_id       SERIAL PRIMARY KEY,
    user_id       INTEGER,
    date          DATE,
    goal_type     VARCHAR(50),
    target_value  INTEGER,
    actual_value  INTEGER,
    status        VARCHAR(10)
);