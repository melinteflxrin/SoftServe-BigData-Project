INSERT INTO raw.user_profile 
(name, age, weight_kg, height_cm, gender, calorie_goal, macro_goal)
VALUES (%s, %s, %s, %s, %s, %s, %s)
RETURNING user_id;