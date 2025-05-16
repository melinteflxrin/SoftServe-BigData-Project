INSERT INTO trusted.goals_data (
    goal_id, user_id, user_name, age, gender, date,
    goal_type, target_value, actual_value, status
)
SELECT
    fgl.goal_id,
    fgl.user_id,
    dup.name AS user_name,
    dup.age,
    dup.gender,
    fgl.date,
    fgl.goal_type,
    fgl.target_value,
    fgl.actual_value,
    fgl.status
FROM staging.fact_goals_log fgl
JOIN staging.dim_user_profile dup ON fgl.user_id = dup.user_id;