DELETE FROM trusted.user_data_pii
WHERE user_id IN (SELECT user_id FROM archive.user_data_pii_archive);