CREATE TABLE IF NOT EXISTS staging.dim_food_item (
    food_item_id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    food_item VARCHAR(255) NOT NULL UNIQUE,
    calories_per_100g DECIMAL(4,0),
    carbs_per_100g DECIMAL(3,0),
    protein_per_100g DECIMAL(3,0),
    fat_per_100g DECIMAL(3,0)
);