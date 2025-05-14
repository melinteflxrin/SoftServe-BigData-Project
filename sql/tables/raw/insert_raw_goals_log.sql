INSERT INTO raw.goals_log 
(user_id, date, goal_type, target_value, actual_value, status)
VALUES (%s, %s, %s, %s, %s, %s);