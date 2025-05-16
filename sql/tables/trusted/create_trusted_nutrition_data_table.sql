CREATE TABLE IF NOT EXISTS trusted.nutrition_data (
    nutrition_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255),
    age INT,
    gender VARCHAR(50),
    date DATE NOT NULL,
    food_item VARCHAR(255),
    meal_type VARCHAR(100),
    calories_per_100g DECIMAL(4,0),
    carbs_per_100g DECIMAL(3,0),
    protein_per_100g DECIMAL(3,0),
    fat_per_100g DECIMAL(3,0)
);