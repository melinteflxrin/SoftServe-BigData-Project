CREATE TABLE IF NOT EXISTS raw.user_data (
    record_id           SERIAL PRIMARY KEY,
    user_id             INTEGER NOT NULL,
    name                VARCHAR(100),
    age                 INTEGER,
    weight_kg           NUMERIC(4,1),
    height_cm           NUMERIC(4,1),
    gender              VARCHAR(10),
    calorie_goal        INTEGER,
    macro_goal          JSON,
    activity_start      TIMESTAMP NOT NULL,
    activity_type       VARCHAR(50),
    steps               INTEGER,
    heart_rate          INTEGER,
    calories_burned     INTEGER,
    sleep_start         TIMESTAMP,
    sleep_end           TIMESTAMP,
    sleep_quality_score INTEGER,
    goal_type           VARCHAR(50),
    goal_target         INTEGER,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);