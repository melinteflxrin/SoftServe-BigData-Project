INSERT INTO archive.user_data_pii_archive (user_id, name, age, gender)
SELECT user_id, name, age, gender
FROM trusted.user_profile
WHERE age > 50
  AND user_id NOT IN (SELECT user_id FROM archive.user_data_pii_archive);