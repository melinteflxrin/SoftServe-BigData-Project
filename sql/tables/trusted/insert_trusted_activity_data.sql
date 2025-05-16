INSERT INTO trusted.activity_data (
    activity_id, user_id, user_name, age, gender, timestamp,
    activity_type, steps, heart_rate, calories_burned
)
SELECT
    fal.activity_id,
    fal.user_id,
    dup.name AS user_name,
    dup.age,
    dup.gender,
    fal.timestamp,
    fal.activity_type,
    fal.steps,
    fal.heart_rate,
    fal.calories_burned
FROM staging.fact_activity_log fal
JOIN staging.dim_user_profile dup ON fal.user_id = dup.user_id
ON CONFLICT (activity_id) DO NOTHING;