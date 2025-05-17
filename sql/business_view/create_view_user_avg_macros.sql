CREATE OR REPLACE VIEW trusted.vw_user_avg_macros AS
SELECT
    n.user_id,
    u.name AS user_name,
    ROUND(AVG(n.calories_per_100g),1) AS avg_calories_per_100g,
    ROUND(AVG(n.carbs_per_100g),1) AS avg_carbs_per_100g,
    ROUND(AVG(n.protein_per_100g),1) AS avg_protein_per_100g,
    ROUND(AVG(n.fat_per_100g),1) AS avg_fat_per_100g
FROM
    trusted.nutrition_data n
    JOIN trusted.user_profile u ON n.user_id = u.user_id
GROUP BY
    n.user_id,
    u.name;