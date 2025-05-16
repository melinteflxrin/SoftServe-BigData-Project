CREATE OR REPLACE VIEW trusted.vw_pct_users_achieved_goals AS
WITH user_goals AS (
    SELECT
        user_id,
        user_name,
        goal_type,
        date,
        target_value,
        actual_value
    FROM
        trusted.goals_data
)
, goal_stats AS (
    SELECT
        COUNT(*) AS total_goals,
        COUNT(*) FILTER (WHERE actual_value >= target_value) AS goals_achieved
    FROM
        user_goals
)
SELECT
    ROUND(100.0 * goals_achieved / NULLIF(total_goals, 0), 2) AS pct_users_achieved_goals
FROM
    goal_stats;