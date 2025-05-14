CREATE TABLE IF NOT EXISTS raw.user_profile (
    user_id         SERIAL PRIMARY KEY,
    name            VARCHAR(100),
    age             INTEGER,
    weight_kg       NUMERIC(4,1),
    height_cm       NUMERIC(4,1),
    gender          VARCHAR(10),
    calorie_goal    INTEGER,
    macro_goal      JSON
);