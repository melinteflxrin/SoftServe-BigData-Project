import psycopg2
from dotenv import load_dotenv
import os

class TrustedDataLoader:
    """Handle creation and population of trusted layer tables."""

    def __init__(self):
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
        self.conn = psycopg2.connect(**self.db_config)

    def close_db(self):
        if self.conn:
            self.conn.close()

    @staticmethod
    def load_sql(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def execute_sql(self, sql_file):
        sql = self.load_sql(sql_file)
        with self.conn.cursor() as crs:
            crs.execute(sql)
            print(f"Executed SQL from {sql_file}")

    def create_trusted_tables(self):
        """Create all trusted tables."""
        try:
            print("Ensuring trusted tables exist...")
            base_path = os.path.join(os.path.dirname(__file__), '../../sql/tables/trusted/')
            self.execute_sql(os.path.join(base_path, 'create_trusted_nutrition_data_table.sql'))
            self.execute_sql(os.path.join(base_path, 'create_trusted_sleep_data_table.sql'))
            self.execute_sql(os.path.join(base_path, 'create_trusted_activity_data_table.sql'))
            self.execute_sql(os.path.join(base_path, 'create_trusted_goals_data_table.sql'))
            self.conn.commit()
            print("Trusted table creation completed successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error during trusted table creation: {e}")
            raise

    def insert_trusted_data(self):
        """Insert data into trusted tables."""
        try:
            print("Loading data into trusted tables...")
            base_path = os.path.join(os.path.dirname(__file__), '../../sql/tables/trusted/')
            self.execute_sql(os.path.join(base_path, 'insert_trusted_nutrition_data.sql'))
            self.execute_sql(os.path.join(base_path, 'insert_trusted_sleep_data.sql'))
            self.execute_sql(os.path.join(base_path, 'insert_trusted_activity_data.sql'))
            self.execute_sql(os.path.join(base_path, 'insert_trusted_goals_data.sql'))
            self.conn.commit()
            print("Trusted data loading completed successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error during trusted data loading: {e}")
            raise

    def run_trusted_load(self):
        """Run the full trusted layer load process."""
        try:
            self.connect_db()
            self.create_trusted_tables()
            self.insert_trusted_data()
        finally:
            self.close_db()

if __name__ == "__main__":
    loader = TrustedDataLoader()
    loader.run_trusted_load()