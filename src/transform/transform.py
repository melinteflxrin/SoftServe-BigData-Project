import psycopg2
from dotenv import load_dotenv
import os


class DatabaseTransformer:
    """handle database transformations, including table creation and data insertion."""

    def __init__(self):
        """initialize the DatabaseTransformer with database configuration."""
        load_dotenv()
        self.db_config = {
            'dbname': os.getenv('DB_NAME', 'health_fitness_db'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', 'placeholder_password'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', 5432)
        }
        self.conn = None

    def connect_db(self):
        """establish connection to the database."""
        self.conn = psycopg2.connect(**self.db_config)

    def close_db(self):
         """close database connection."""
        if self.conn:
            self.conn.close()

    @staticmethod
    def load_sql(file_path):
        """load SQL from a file."""
        with open(file_path, 'r') as file:
            return file.read()

    def execute_sql(self, sql_file):
        """execute SQL from a file."""
        sql = self.load_sql(sql_file)
        with self.conn.cursor() as crs:
            crs.execute(sql)
            print(f"Executed SQL from {sql_file}")

    def create_tables(self):
        """create all necessary tables in the database."""
        try:
            print("Ensuring tables exist...")
            base_path = os.path.join(os.path.dirname(__file__), '../../sql/tables/staging/')
            self.execute_sql(os.path.join(base_path, 'create_dim_user_profile_table.sql'))
            self.execute_sql(os.path.join(base_path, 'create_fact_activity_log_table.sql'))
            self.execute_sql(os.path.join(base_path, 'create_fact_sleep_log_table.sql'))
            self.execute_sql(os.path.join(base_path, 'create_fact_nutrition_log_table.sql'))
            self.execute_sql(os.path.join(base_path, 'create_fact_goals_log_table.sql'))
            self.conn.commit()
            print("Table creation completed successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error during table creation: {e}")
            raise

    def insert_data(self):
        """insert transformed data into the database tables."""
        try:
            print("Transforming data...")
            base_path = os.path.join(os.path.dirname(__file__), '../../sql/tables/staging/')
            self.execute_sql(os.path.join(base_path, 'insert_dim_user_profile.sql'))
            self.execute_sql(os.path.join(base_path, 'insert_fact_activity_log.sql'))
            self.execute_sql(os.path.join(base_path, 'insert_fact_sleep_log.sql'))
            self.execute_sql(os.path.join(base_path, 'insert_fact_nutrition_log.sql'))
            self.execute_sql(os.path.join(base_path, 'insert_fact_goals_log.sql'))
            self.conn.commit()
            print("Data transformation completed successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error during data transformation: {e}")
            raise

    def run_transformations(self):
         """run the full transformation process: creating tables and inserting data."""
        try:
            self.connect_db()
            self.create_tables()
            self.insert_data()
        finally:
            self.close_db()


if __name__ == "__main__":
    transformer = DatabaseTransformer()
    transformer.run_transformations()