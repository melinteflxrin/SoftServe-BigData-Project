CREATE OR REPLACE VIEW trusted.vw_user_daily_avg_calories_burned AS
SELECT
    a.user_id,
    u.name AS user_name,
    ROUND(AVG(a.calories_burned), 1) AS avg_calories_burned
FROM
    trusted.activity_data a
    JOIN trusted.user_profile u ON a.user_id = u.user_id
GROUP BY
    a.user_id,
    u.name;