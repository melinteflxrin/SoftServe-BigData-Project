INSERT INTO trusted.activity_data (
    activity_id, user_id, timestamp,
    activity_type, steps, heart_rate, calories_burned
)
SELECT
    fal.activity_id,
    fal.user_id,
    fal.timestamp,
    fal.activity_type,
    fal.steps,
    fal.heart_rate,
    fal.calories_burned
FROM staging.fact_activity_log fal
ON CONFLICT (activity_id) DO NOTHING;