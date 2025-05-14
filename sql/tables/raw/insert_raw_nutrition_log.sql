INSERT INTO raw.nutrition_log 
(user_id, date, food_item, meal_type, calories_per_100g, carbs_per_100g, protein_per_100g, fat_per_100g)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);