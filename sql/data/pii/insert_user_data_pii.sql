INSERT INTO trusted.user_data_pii (user_id, name, age, gender)
SELECT user_id, name, age, gender
FROM trusted.user_profile
WHERE user_id IS NOT NULL
  AND name IS NOT NULL
  AND age IS NOT NULL
ON CONFLICT (user_id) DO NOTHING;