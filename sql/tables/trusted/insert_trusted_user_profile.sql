INSERT INTO trusted.user_profile (
    user_id, name, age, gender
)
SELECT DISTINCT
    user_id, name, age, gender
FROM staging.dim_user_profile
ON CONFLICT (user_id) DO UPDATE
SET
    name = EXCLUDED.name,
    age = EXCLUDED.age,
    gender = EXCLUDED.gender;