INSERT INTO staging.fact_nutrition_log (
    nutrition_id,
    user_id,
    date,
    food_item_id,
    meal_type
)
SELECT
    n.nutrition_id,
    n.user_id,
    n.date,
    d.food_item_id,
    INITCAP(TRIM(n.meal_type)) AS meal_type
FROM raw.nutrition_log n
JOIN staging.dim_food_item d
  ON INITCAP(TRIM(n.food_item)) = d.food_item
WHERE n.nutrition_id IS NOT NULL
ON CONFLICT (nutrition_id)
DO UPDATE SET
    user_id = EXCLUDED.user_id,
    date = EXCLUDED.date,
    food_item_id = EXCLUDED.food_item_id,
    meal_type = EXCLUDED.meal_type;