CREATE OR REPLACE VIEW trusted.vw_pct_users_achieved_goals AS
WITH user_goals AS (
    SELECT
        gd.user_id,
        up.name AS user_name,
        gd.goal_type,
        gd.date,
        gd.target_value,
        gd.actual_value
    FROM
        trusted.goals_data gd
        JOIN trusted.user_profile up ON gd.user_id = up.user_id
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