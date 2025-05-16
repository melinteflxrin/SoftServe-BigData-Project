INSERT INTO trusted.sleep_data (
    sleep_id, user_id, user_name, age, gender, date,
    sleep_start, sleep_end, sleep_duration_hours, sleep_quality_score
)
SELECT
    fsl.sleep_id,
    fsl.user_id,
    dup.name AS user_name,
    dup.age,
    dup.gender,
    fsl.date,
    fsl.sleep_start,
    fsl.sleep_end,
    fsl.sleep_duration_hours,
    fsl.sleep_quality_score
FROM staging.fact_sleep_log fsl
JOIN staging.dim_user_profile dup ON fsl.user_id = dup.user_id
ON CONFLICT (sleep_id) DO NOTHING;