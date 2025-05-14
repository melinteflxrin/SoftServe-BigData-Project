CREATE TABLE IF NOT EXISTS staging.user_profile AS
SELECT
    user_id,
    INITCAP(TRIM(name)) AS name,
    age,
    weight_kg,
    height_cm,
    LOWER(TRIM(gender)) AS gender,
    calorie_goal,
    (macro_goal->>'carbs')::INTEGER AS carbs_goal,
    (macro_goal->>'protein')::INTEGER AS protein_goal,
    (macro_goal->>'fat')::INTEGER AS fat_goal
FROM raw.user_profile
WHERE name IS NOT NULL;