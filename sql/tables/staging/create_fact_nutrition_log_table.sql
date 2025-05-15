CREATE TABLE IF NOT EXISTS staging.fact_nutrition_log (
    nutrition_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    date DATE NOT NULL,
    food_item VARCHAR(255),
    meal_type VARCHAR(100),
    calories_per_100g DECIMAL(4,0),
    carbs_per_100g DECIMAL(3,0),
    protein_per_100g DECIMAL(3,0),
    fat_per_100g DECIMAL(3,0)
);