"""
For testing purposes, this script clears all data from the staging tables.
"""
TRUNCATE TABLE staging.user_profile RESTART IDENTITY CASCADE;
DELETE FROM staging.activity_log;
DELETE FROM staging.sleep_log;
DELETE FROM staging.nutrition_log;
DELETE FROM staging.goals_log;
