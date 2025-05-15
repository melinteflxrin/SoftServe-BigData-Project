INSERT INTO staging.fact_activity_log (
    activity_id,
    user_id,
    timestamp,
    activity_type,
    steps,
    heart_rate,
    calories_burned
)
SELECT
    record_id AS activity_id, 
    user_id,
    activity_start AS timestamp,
    INITCAP(TRIM(activity_type)) AS activity_type, 
    steps,
    heart_rate,
    calories_burned
FROM raw.user_data
WHERE activity_start IS NOT NULL
ON CONFLICT (activity_id) 
DO UPDATE SET
    user_id = EXCLUDED.user_id,
    timestamp = EXCLUDED.timestamp,
    activity_type = EXCLUDED.activity_type,
    steps = EXCLUDED.steps,
    heart_rate = EXCLUDED.heart_rate,
    calories_burned = EXCLUDED.calories_burned;