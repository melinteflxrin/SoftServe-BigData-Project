INSERT INTO trusted.nutrition_data (
    nutrition_id, user_id, user_name, age, gender, date,
    food_item, meal_type, calories_per_100g, carbs_per_100g, protein_per_100g, fat_per_100g
)
SELECT
    fnl.nutrition_id,
    fnl.user_id,
    dup.name AS user_name,
    dup.age,
    dup.gender,
    fnl.date,
    dfi.food_item,
    fnl.meal_type,
    dfi.calories_per_100g,
    dfi.carbs_per_100g,
    dfi.protein_per_100g,
    dfi.fat_per_100g
FROM staging.fact_nutrition_log fnl
JOIN staging.dim_user_profile dup ON fnl.user_id = dup.user_id
JOIN staging.dim_food_item dfi ON fnl.food_item_id = dfi.food_item_id
ON CONFLICT (nutrition_id) DO NOTHING;