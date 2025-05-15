"""
For testing purposes, this script clears all data from the staging tables.
"""
DROP TABLE IF EXISTS staging.fact_goals_log;
DROP TABLE IF EXISTS staging.fact_sleep_log;
DROP TABLE IF EXISTS staging.fact_activity_log;
DROP TABLE IF EXISTS staging.fact_nutrition_log;
DROP TABLE IF EXISTS staging.dim_user_profile;


TRUNCATE TABLE staging.user_profile RESTART IDENTITY CASCADE;
DELETE FROM staging.activity_log;
DELETE FROM staging.sleep_log;
DELETE FROM staging.nutrition_log;
DELETE FROM staging.goals_log;
