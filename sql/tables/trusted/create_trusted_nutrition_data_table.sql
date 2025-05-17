CREATE TABLE IF NOT EXISTS trusted.nutrition_data (
    nutrition_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK (age > 0),
    gender VARCHAR(50) NOT NULL CHECK (gender IN ('male', 'female', 'other')),
    date DATE NOT NULL,
    food_item VARCHAR(255) NOT NULL,
    meal_type VARCHAR(100),
    calories_per_100g DECIMAL(4,0) NOT NULL CHECK (calories_per_100g >= 0),
    carbs_per_100g DECIMAL(3,0) NOT NULL CHECK (carbs_per_100g >= 0),
    protein_per_100g DECIMAL(3,0) NOT NULL CHECK (protein_per_100g >= 0),
    fat_per_100g DECIMAL(3,0) NOT NULL CHECK (fat_per_100g >= 0)
);