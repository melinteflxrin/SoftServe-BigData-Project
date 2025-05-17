INSERT INTO trusted.goals_data (
    goal_id, user_id, date,
    goal_type, target_value, actual_value, status
)
SELECT
    fgl.goal_id,
    fgl.user_id,
    fgl.date,
    fgl.goal_type,
    fgl.target_value,
    fgl.actual_value,
    fgl.status
FROM staging.fact_goals_log fgl
ON CONFLICT (goal_id) DO NOTHING;