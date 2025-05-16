"""
For testing purposes, this script clears all data from the trusted tables.
"""
DROP TABLE IF EXISTS trusted.goals_data;
DROP TABLE IF EXISTS trusted.sleep_data;
DROP TABLE IF EXISTS trusted.activity_data;
DROP TABLE IF EXISTS trusted.nutrition_data;

TRUNCATE TABLE 
   trusted.goals_data,
   trusted.sleep_data,
   trusted.activity_data,
   trusted.nutrition_data
RESTART IDENTITY CASCADE;