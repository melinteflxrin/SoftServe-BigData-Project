INSERT INTO raw.activity_log 
(user_id, timestamp, activity_type, steps, heart_rate, calories_burned)
VALUES (%s, %s, %s, %s, %s, %s);