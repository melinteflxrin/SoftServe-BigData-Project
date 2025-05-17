INSERT INTO trusted.user_data_non_pii (user_hash, gender, age_group)
SELECT
    md5(CAST(user_id AS TEXT)) AS user_hash,
    gender,
    CASE
        WHEN age < 20 THEN 'under_20'
        WHEN age < 30 THEN '20s'
        WHEN age < 40 THEN '30s'
        WHEN age < 50 THEN '40s'
        ELSE '50_plus'
    END AS age_group
FROM trusted.user_profile
ON CONFLICT (user_hash) DO NOTHING;