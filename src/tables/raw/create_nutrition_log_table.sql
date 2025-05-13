CREATE TABLE raw.nutrition_log (
    nutrition_id  SERIAL PRIMARY KEY,
    user_id       INTEGER,
    date          DATE,
    food_item     VARCHAR(100),
    meal_type     VARCHAR(20),
    calories      INTEGER,
    carbs         INTEGER,
    protein       INTEGER,
    fat           INTEGER
);