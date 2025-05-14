CREATE TABLE raw.user_profile (
    user_id         SERIAL PRIMARY KEY,
    name            VARCHAR(100),
    age             INTEGER,
    weight          NUMERIC(5,1),
    height          NUMERIC(5,1),
    gender          VARCHAR(10),
    calorie_goal    INTEGER,
    macro_goal      JSON
);