CREATE TABLE staging.goals_log AS
SELECT
    goal_id,
    user_id,
    date,
    LOWER(TRIM(goal_type)) AS goal_type,
    target_value,
    actual_value,
    LOWER(TRIM(status)) AS status
FROM raw.goals_log
WHERE user_id IS NOT NULL
  AND goal_type IS NOT NULL;