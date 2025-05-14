CREATE TABLE IF NOT EXISTS raw.nutrition_log (
    nutrition_id       SERIAL PRIMARY KEY,
    user_id            INTEGER,
    date               DATE,
    food_item          VARCHAR(100),
    meal_type          VARCHAR(20),
    calories_per_100g  INTEGER,
    carbs_per_100g     INTEGER,
    protein_per_100g   INTEGER,
    fat_per_100g       INTEGER
);