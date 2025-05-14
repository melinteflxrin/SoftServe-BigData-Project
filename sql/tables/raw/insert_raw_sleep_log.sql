INSERT INTO raw.sleep_log 
(user_id, date, sleep_start, sleep_end, sleep_quality_score)
VALUES (%s, %s, %s, %s, %s);