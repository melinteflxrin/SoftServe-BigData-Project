CREATE OR REPLACE VIEW trusted.vw_user_avg_macros AS
SELECT
    user_id,
    user_name,
    ROUND(AVG(calories_per_100g),1) AS avg_calories_per_100g,
    ROUND(AVG(carbs_per_100g),1) AS avg_carbs_per_100g,
    ROUND(AVG(protein_per_100g),1) AS avg_protein_per_100g,
    ROUND(AVG(fat_per_100g),1) AS avg_fat_per_100g
FROM
    trusted.nutrition_data
GROUP BY
    user_id,
    user_name;