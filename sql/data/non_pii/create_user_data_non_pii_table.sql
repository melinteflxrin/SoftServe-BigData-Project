CREATE TABLE IF NOT EXISTS trusted.user_data_non_pii (
    user_hash VARCHAR(64) PRIMARY KEY,
    gender VARCHAR(50),
    age_group VARCHAR(20)
);