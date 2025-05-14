TRUNCATE TABLE raw.user_profile RESTART IDENTITY CASCADE;
DELETE FROM raw.activity_log;
DELETE FROM raw.sleep_log;
DELETE FROM raw.nutrition_log;
DELETE FROM raw.goals_log;
