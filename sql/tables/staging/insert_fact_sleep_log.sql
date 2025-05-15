INSERT INTO staging.fact_sleep_log (
    sleep_id,
    user_id,
    date,
    sleep_start,
    sleep_end,
    sleep_duration_hours,
    sleep_quality_score
)
SELECT
    record_id AS sleep_id, 
    user_id,
    sleep_start::DATE AS date, 
    sleep_start, 
    sleep_end, 
    ROUND(EXTRACT(EPOCH FROM (sleep_end - sleep_start)) / 3600, 1) AS sleep_duration_hours, 
    sleep_quality_score
FROM raw.user_data
WHERE sleep_start IS NOT NULL AND sleep_end IS NOT NULL
    AND user_id IS NOT NULL
    AND sleep_end > sleep_start
ON CONFLICT (sleep_id) 
DO UPDATE SET
    user_id = EXCLUDED.user_id,
    date = EXCLUDED.date,
    sleep_start = EXCLUDED.sleep_start,
    sleep_end = EXCLUDED.sleep_end,
    sleep_duration_hours = EXCLUDED.sleep_duration_hours,
    sleep_quality_score = EXCLUDED.sleep_quality_score;