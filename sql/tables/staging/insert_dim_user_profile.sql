INSERT INTO staging.dim_user_profile (
    user_id,
    name,
    age,
    weight_kg,
    height_cm,
    gender,
    calorie_goal,
    carbs_goal,
    protein_goal,
    fat_goal
)
SELECT
    user_id,
    INITCAP(TRIM(MAX(name))) AS name, 
    MAX(age) AS age, 
    MAX(weight_kg) AS weight_kg,
    MAX(height_cm) AS height_cm, 
    LOWER(TRIM(MAX(gender))) AS gender,
    MAX(calorie_goal) AS calorie_goal, 
    MAX((macro_goal->>'carbs')::INT) AS carbs_goal, 
    MAX((macro_goal->>'protein')::INT) AS protein_goal, 
    MAX((macro_goal->>'fat')::INT) AS fat_goal 
FROM raw.user_data
WHERE user_id IS NOT NULL
GROUP BY user_id
ON CONFLICT (user_id)
DO UPDATE SET
    name = EXCLUDED.name,
    age = EXCLUDED.age,
    weight_kg = EXCLUDED.weight_kg,
    height_cm = EXCLUDED.height_cm,
    gender = EXCLUDED.gender,
    calorie_goal = EXCLUDED.calorie_goal,
    carbs_goal = EXCLUDED.carbs_goal,
    protein_goal = EXCLUDED.protein_goal,
    fat_goal = EXCLUDED.fat_goal;