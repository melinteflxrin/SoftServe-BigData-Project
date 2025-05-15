"""
For testing purposes, this script clears all data from the staging tables.
"""
DROP TABLE IF EXISTS staging.fact_goals_log;
DROP TABLE IF EXISTS staging.fact_sleep_log;
DROP TABLE IF EXISTS staging.fact_activity_log;
DROP TABLE IF EXISTS staging.fact_nutrition_log;
DROP TABLE IF EXISTS staging.dim_user_profile;


DELETE FROM staging.dim_user_profile;
DELETE FROM staging.fact_activity_log;
DELETE FROM staging.fact_sleep_log;
DELETE FROM staging.fact_nutrition_log;
DELETE FROM staging.fact_goals_log;