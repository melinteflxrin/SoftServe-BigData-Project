INSERT INTO trusted.sleep_data (
    sleep_id, user_id, date,
    sleep_start, sleep_end, sleep_duration_hours, sleep_quality_score
)
SELECT
    fsl.sleep_id,
    fsl.user_id,
    fsl.date,
    fsl.sleep_start,
    fsl.sleep_end,
    fsl.sleep_duration_hours,
    fsl.sleep_quality_score
FROM staging.fact_sleep_log fsl
ON CONFLICT (sleep_id) DO NOTHING;