import psycopg2
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# database configuration
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'health_fitness_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'placeholder_password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432)
}

def connect_db():
    """Connect to the database."""
    return psycopg2.connect(**DB_CONFIG)

def load_sql(file_path):
    """Load SQL from a file."""
    with open(file_path, 'r') as file:
        return file.read()

def execute_sql(conn, sql_file):
    """Execute SQL from a file."""
    sql = load_sql(sql_file)
    with conn.cursor() as crs:
        crs.execute(sql)
        print(f"Executed SQL from {sql_file}")

def run_transformations():
    """Run all transformation scripts."""
    conn = connect_db()
    try:
        print("Ensuring tables exist...")
        base_path = os.path.join(os.path.dirname(__file__), '../../sql/tables/staging/')
        # create tables if they dont already exist
        execute_sql(conn, os.path.join(base_path, 'create_stg_user_profile_table.sql'))
        execute_sql(conn, os.path.join(base_path, 'create_stg_activity_log_table.sql'))
        execute_sql(conn, os.path.join(base_path, 'create_stg_sleep_log_table.sql'))
        execute_sql(conn, os.path.join(base_path, 'create_stg_nutrition_log_table.sql'))
        execute_sql(conn, os.path.join(base_path, 'create_stg_goals_log_table.sql'))

        print("Transforming data...")
        # insert data into tables
        execute_sql(conn, os.path.join(base_path, 'insert_stg_user_profile.sql'))
        execute_sql(conn, os.path.join(base_path, 'insert_stg_activity_log.sql'))
        execute_sql(conn, os.path.join(base_path, 'insert_stg_sleep_log.sql'))
        execute_sql(conn, os.path.join(base_path, 'insert_stg_nutrition_log.sql'))
        execute_sql(conn, os.path.join(base_path, 'insert_stg_goals_log.sql'))
        conn.commit()
        print("Data transformation completed successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error during data transformation: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_transformations()