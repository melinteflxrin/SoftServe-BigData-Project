CREATE TABLE IF NOT EXISTS trusted.nutrition_data_archive AS
SELECT *
FROM trusted.nutrition_data
WITH NO DATA;