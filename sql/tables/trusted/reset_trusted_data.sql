"""
For testing purposes, this script clears all data from the trusted tables.
"""
TRUNCATE TABLE 
   trusted.user_profile,
   trusted.goals_data,
   trusted.sleep_data,
   trusted.activity_data,
   trusted.nutrition_data
RESTART IDENTITY CASCADE;

DROP TABLE IF EXISTS trusted.user_profile CASCADE;
DROP TABLE IF EXISTS trusted.goals_data CASCADE;
DROP TABLE IF EXISTS trusted.sleep_data CASCADE;
DROP TABLE IF EXISTS trusted.activity_data CASCADE;
DROP TABLE IF EXISTS trusted.nutrition_data CASCADE;

