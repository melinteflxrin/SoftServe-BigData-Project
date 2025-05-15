INSERT INTO staging.fact_goals_log (
    goal_id,
    user_id,
    date,
    goal_type,
    target_value,
    actual_value,
    status
)
SELECT
    record_id AS goal_id, 
    user_id,
    created_at::DATE AS date, 
    INITCAP(TRIM(goal_type)) AS goal_type, 
    goal_target AS target_value,
    CASE 
        WHEN UPPER(TRIM(goal_type)) = 'CALORIES BURNED' THEN calories_burned
        WHEN UPPER(TRIM(goal_type)) = 'HOURS SLEPT' THEN
            EXTRACT(EPOCH FROM (sleep_end - sleep_start)) / 3600 
        WHEN UPPER(TRIM(goal_type)) = 'STEPS TAKEN' THEN steps
        ELSE NULL
    END AS actual_value, 
    CASE 
        WHEN UPPER(TRIM(goal_type)) = 'CALORIES BURNED' AND calories_burned >= goal_target THEN 'ACHIEVED'
        WHEN UPPER(TRIM(goal_type)) = 'CALORIES BURNED' AND calories_burned < goal_target THEN 'NOT ACHIEVED'
        WHEN UPPER(TRIM(goal_type)) = 'HOURS SLEPT' AND 
             EXTRACT(EPOCH FROM (sleep_end - sleep_start)) / 3600 >= goal_target THEN 'ACHIEVED'
        WHEN UPPER(TRIM(goal_type)) = 'HOURS SLEPT' AND 
             EXTRACT(EPOCH FROM (sleep_end - sleep_start)) / 3600 < goal_target THEN 'NOT ACHIEVED'
        WHEN UPPER(TRIM(goal_type)) = 'STEPS TAKEN' AND steps >= goal_target THEN 'ACHIEVED'
        WHEN UPPER(TRIM(goal_type)) = 'STEPS TAKEN' AND steps < goal_target THEN 'NOT ACHIEVED'
        ELSE 'PENDING'
    END AS status 
FROM raw.user_data
WHERE goal_type IS NOT NULL
ON CONFLICT (goal_id) 
DO UPDATE SET
    user_id = EXCLUDED.user_id,
    date = EXCLUDED.date,
    goal_type = EXCLUDED.goal_type,
    target_value = EXCLUDED.target_value,
    actual_value = EXCLUDED.actual_value,
    status = EXCLUDED.status;