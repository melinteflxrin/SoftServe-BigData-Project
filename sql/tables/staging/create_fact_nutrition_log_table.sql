CREATE TABLE IF NOT EXISTS staging.fact_nutrition_log (
    nutrition_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    date DATE NOT NULL,
    food_item_id BIGINT NOT NULL,
    meal_type VARCHAR(100),
    FOREIGN KEY (food_item_id) REFERENCES staging.dim_food_item(food_item_id)
);