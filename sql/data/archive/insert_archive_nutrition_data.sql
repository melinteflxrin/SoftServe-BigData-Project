INSERT INTO trusted.nutrition_data_archive
SELECT * FROM trusted.nutrition_data
WHERE date < CURRENT_DATE - INTERVAL '1 year';