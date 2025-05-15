CREATE TABLE IF NOT EXISTS staging.dim_user_profile (
    user_id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    weight_kg DECIMAL(4, 1),
    height_cm DECIMAL(4, 1),
    gender VARCHAR(50),
    calorie_goal INT,
    carbs_goal INT,
    protein_goal INT,
    fat_goal INT
);