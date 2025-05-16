CREATE OR REPLACE VIEW trusted.vw_user_favourite_food AS
WITH food_counts AS (
    SELECT
        user_id,
        user_name,
        food_item,
        meal_type,
        COUNT(*) AS times_consumed
    FROM
        trusted.nutrition_data
    GROUP BY
        user_id, user_name, food_item, meal_type
),
ranked_foods AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY times_consumed DESC
        ) AS rn
    FROM
        food_counts
)
SELECT
    user_id,
    user_name,
    food_item AS favourite_food,
    meal_type AS usual_meal_time,
    times_consumed
FROM
    ranked_foods
WHERE
    rn = 1;