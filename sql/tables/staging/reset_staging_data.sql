"""
For testing purposes, this script clears all data from the staging tables.
"""
DROP TABLE IF EXISTS staging.fact_goals_log CASCADE;
DROP TABLE IF EXISTS staging.fact_sleep_log CASCADE;
DROP TABLE IF EXISTS staging.fact_activity_log CASCADE;
DROP TABLE IF EXISTS staging.fact_nutrition_log CASCADE;
DROP TABLE IF EXISTS staging.dim_user_profile CASCADE;
DROP TABLE IF EXISTS staging.dim_food_item CASCADE;


DELETE FROM staging.dim_user_profile;
DELETE FROM staging.fact_activity_log;
DELETE FROM staging.fact_sleep_log;
DELETE FROM staging.fact_goals_log;
TRUNCATE TABLE 
    staging.fact_nutrition_log, 
    staging.dim_food_item 
RESTART IDENTITY;