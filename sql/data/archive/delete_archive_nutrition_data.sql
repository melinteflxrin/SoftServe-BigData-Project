DELETE FROM trusted.nutrition_data
WHERE nutrition_id IN (
    SELECT nutrition_id FROM trusted.nutrition_data_archive
);