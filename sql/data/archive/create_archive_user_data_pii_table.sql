CREATE TABLE IF NOT EXISTS archive.user_data_pii_archive (
    user_id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(50),
    archived_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);