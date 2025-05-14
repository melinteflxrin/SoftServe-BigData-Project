INSERT INTO staging.sleep_log (sleep_id, user_id, date, sleep_start, sleep_end, sleep_duration_hours, sleep_quality_score)
SELECT 
    sleep_id, 
    user_id, 
    date, 
    TO_CHAR(sleep_start, 'YYYY-MM-DD HH24:MI') AS sleep_start, 
    TO_CHAR(sleep_end, 'YYYY-MM-DD HH24:MI') AS sleep_end,    
    ROUND(EXTRACT(EPOCH FROM (sleep_end - sleep_start)) / 3600, 1) AS sleep_duration_hours, 
    sleep_quality_score
FROM raw.sleep_log
WHERE user_id IS NOT NULL
  AND sleep_end > sleep_start;