CREATE TABLE staging.sleep_log AS
SELECT
    sleep_id,
    user_id,
    date,
    sleep_start,
    sleep_end,
    EXTRACT(EPOCH FROM (sleep_end - sleep_start)) / 3600 AS sleep_duration_hours,
    sleep_quality_score
FROM raw.sleep_log
WHERE user_id IS NOT NULL
  AND sleep_end > sleep_start;