REVOKE ALL ON trusted.user_data_pii FROM PUBLIC;
GRANT SELECT, INSERT, UPDATE, DELETE ON trusted.user_data_pii TO dba_role;