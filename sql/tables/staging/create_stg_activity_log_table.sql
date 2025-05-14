CREATE TABLE IF NOT EXISTS staging.activity_log AS
SELECT
    activity_id,
    user_id,
    TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI') AS timestamp,
    INITCAP(TRIM(activity_type)) AS activity_type,
    steps,
    heart_rate,
    calories_burned
FROM raw.activity_log
WHERE user_id IS NOT NULL;