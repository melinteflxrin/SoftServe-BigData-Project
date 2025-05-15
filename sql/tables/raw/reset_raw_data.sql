"""
For testing purposes, this script clears all data from the raw tables.
"""
TRUNCATE TABLE raw.user_data RESTART IDENTITY CASCADE;
DELETE FROM raw.nutrition_log;
DROP TABLE IF EXISTS raw.user_data;
DROP TABLE IF EXISTS raw.nutrition_log;