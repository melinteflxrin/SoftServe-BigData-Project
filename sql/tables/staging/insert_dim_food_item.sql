INSERT INTO staging.dim_food_item (food_item, calories_per_100g, carbs_per_100g, protein_per_100g, fat_per_100g)
SELECT DISTINCT
    INITCAP(TRIM(food_item)) AS food_item,
    calories_per_100g,
    carbs_per_100g,
    protein_per_100g,
    fat_per_100g
FROM raw.nutrition_log
WHERE food_item IS NOT NULL
ON CONFLICT (food_item) DO NOTHING;
