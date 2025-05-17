REVOKE ALL ON trusted.user_data_non_pii FROM PUBLIC;
GRANT SELECT ON trusted.user_data_non_pii TO dba_role;