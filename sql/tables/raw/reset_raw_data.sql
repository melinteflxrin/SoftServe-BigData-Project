"""
For testing purposes, this script clears all data from the raw tables.
"""
TRUNCATE TABLE raw.user_data RESTART IDENTITY CASCADE;
TRUNCATE TABLE raw.nutrition_log RESTART IDENTITY CASCADE;
