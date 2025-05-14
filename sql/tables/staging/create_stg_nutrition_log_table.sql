CREATE TABLE staging.nutrition_log AS
SELECT
     nutrition_id,
    user_id,
    date,
    INITCAP(TRIM(food_item)) AS food_item,
    LOWER(TRIM(meal_type)) AS meal_type,
    calories_per_100g,
    carbs_per_100g,
    protein_per_100g,
    fat_per_100g
FROM raw.nutrition_log
WHERE user_id IS NOT NULL
  AND food_item IS NOT NULL;