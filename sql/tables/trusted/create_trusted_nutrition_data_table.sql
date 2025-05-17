CREATE TABLE IF NOT EXISTS trusted.nutrition_data (
    nutrition_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES trusted.user_profile(user_id),
    date DATE NOT NULL,
    food_item VARCHAR(255) NOT NULL,
    meal_type VARCHAR(100),
    calories_per_100g DECIMAL(4,0) NOT NULL CHECK (calories_per_100g >= 0),
    carbs_per_100g DECIMAL(3,0) NOT NULL CHECK (carbs_per_100g >= 0),
    protein_per_100g DECIMAL(3,0) NOT NULL CHECK (protein_per_100g >= 0),
    fat_per_100g DECIMAL(3,0) NOT NULL CHECK (fat_per_100g >= 0)
);