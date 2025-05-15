INSERT INTO staging.fact_nutrition_log (
    nutrition_id,
    user_id,
    date,
    food_item,
    meal_type,
    calories_per_100g,
    carbs_per_100g,
    protein_per_100g,
    fat_per_100g
)
SELECT
    nutrition_id,
    user_id,
    date,
    INITCAP(TRIM(food_item)) AS food_item, 
    INITCAP(TRIM(meal_type)) AS meal_type, 
    calories_per_100g,
    carbs_per_100g,
    protein_per_100g,
    fat_per_100g
FROM raw.nutrition_log
WHERE nutrition_id IS NOT NULL
ON CONFLICT (nutrition_id)
DO UPDATE SET
    user_id = EXCLUDED.user_id,
    date = EXCLUDED.date,
    food_item = EXCLUDED.food_item,
    meal_type = EXCLUDED.meal_type,
    calories_per_100g = EXCLUDED.calories_per_100g,
    carbs_per_100g = EXCLUDED.carbs_per_100g,
    protein_per_100g = EXCLUDED.protein_per_100g,
    fat_per_100g = EXCLUDED.fat_per_100g;