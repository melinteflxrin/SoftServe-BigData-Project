CREATE OR REPLACE VIEW trusted.vw_user_daily_avg_calories_burned AS
SELECT
    user_id,
    user_name,
    ROUND(AVG(calories_burned),1) AS avg_calories_burned
FROM
    trusted.activity_data
GROUP BY
    user_id,
    user_name;