import psycopg2
import random
import json
import os
from datetime import datetime, timedelta
from faker import Faker
from dotenv import load_dotenv
from search_foods_api import fetch_food_nutrition
from load_data_from_csv import load_food_items_from_csv, load_activity_types_from_csv


class DatabaseManager:
    def __init__(self):
        load_dotenv()
        self.db_config = {
            'dbname': os.getenv('DB_NAME', 'health_fitness_db'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', 'placeholder_password'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', 5432)
        }

    def connect(self):
        return psycopg2.connect(**self.db_config)

    @staticmethod
    def load_sql(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def execute_sql(self, conn, sql_file):
        sql = self.load_sql(sql_file)
        with conn.cursor() as crs:
            crs.execute(sql)
            print(f"Executed SQL from {sql_file}")

    def ensure_schemas_exist(self, conn):
        base_path = os.path.join(os.path.dirname(__file__), '../../sql/schemas/')
        self.execute_sql(conn, os.path.join(base_path, 'create_raw_schema.sql'))
        self.execute_sql(conn, os.path.join(base_path, 'create_staging_schema.sql'))
        self.execute_sql(conn, os.path.join(base_path, 'create_trusted_schema.sql'))

    def ensure_tables_exist(self, conn):
        base_path = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/')
        self.execute_sql(conn, os.path.join(base_path, 'create_raw_user_data_table.sql'))
        self.execute_sql(conn, os.path.join(base_path, 'create_raw_nutrition_log_table.sql'))


class UserProfileGenerator:
    def __init__(self, num_users=2):
        self.num_users = num_users
        self.fake = Faker()

    def generate_user_profile(self, user_id=None):
        if user_id is None:
            user_id = random.randint(1, 1000000)

        return {
            'user_id': user_id,
            'name': self.fake.name(),
            'age': random.randint(18, 75),
            'weight_kg': round(random.uniform(50, 150), 1),
            'height_cm': round(random.uniform(150, 220), 1),
            'gender': random.choice(['Male', 'Female']),
            'calorie_goal': random.randint(1500, 3500),
            'macro_goal': json.dumps({
                'carbs': random.randint(200, 450),
                'protein': random.randint(50, 280),
                'fat': random.randint(40, 120)
            })
        }

    def generate_user_profiles(self):
        return [self.generate_user_profile() for _ in range(self.num_users)]


class DataInserter:
    def __init__(self, conn, days=2):
        self.conn = conn
        self.days = days

    def insert_user_data(self, users):
        sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_user_data.sql')
        activity_types = load_activity_types_from_csv('activity_types.csv')
        if not activity_types:
            print("No activity types found in the CSV file. Skipping user data insertion.")
            return

        with self.conn.cursor() as crs:
            for user in users:
                for i in range(self.days):
                    activity_start = datetime.now() - timedelta(days=i)
                    activity_type = random.choice(activity_types)
                    steps = random.randint(1000, 25000)
                    heart_rate = random.randint(60, 150)
                    calories_burned = random.randint(150, 800)

                    sleep_start = datetime.now() - timedelta(hours=random.randint(0, 2))
                    sleep_end = sleep_start + timedelta(hours=random.uniform(6.0, 9.0))
                    sleep_quality_score = random.randint(50, 100)

                    goal_type = random.choice(['calories burned', 'hours slept', 'steps taken'])
                    goal_target = {
                        'calories burned': random.randint(150, 800),
                        'hours slept': round(random.uniform(6.0, 9.0), 1),
                        'steps taken': random.randint(1000, 25000)
                    }.get(goal_type, None)

                    crs.execute(DatabaseManager.load_sql(sql_file), (
                        user['user_id'], user['name'], user['age'], user['weight_kg'], user['height_cm'],
                        user['gender'], user['calorie_goal'], user['macro_goal'], activity_start, activity_type,
                        steps, heart_rate, calories_burned, sleep_start, sleep_end, sleep_quality_score, goal_type,
                        goal_target
                    ))

    def insert_nutrition_log(self, users):
        sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_nutrition_log.sql')
        meals = ['breakfast', 'lunch', 'dinner', 'snack']
        food_items = load_food_items_from_csv('food_items_keywords.csv')
        if not food_items:
            print("No food items found in the CSV file. Skipping nutrition log insertion.")
            return

        with self.conn.cursor() as crs:
            for user in users:
                for i in range(self.days):
                    for meal in meals:
                        food_item = random.choice(food_items)
                        nutrition = fetch_food_nutrition(food_item)
                        if nutrition:
                            crs.execute(DatabaseManager.load_sql(sql_file), (
                                user['user_id'], datetime.now().date() - timedelta(days=i),
                                nutrition['description'], meal,
                                nutrition['calories'], nutrition['carbs'],
                                nutrition['protein'], nutrition['fat']
                            ))
                        else:
                            print(f"Skipping {food_item} due to missing nutritional data.")


def main():
    db_manager = DatabaseManager()
    conn = db_manager.connect()

    try:
        print("Ensuring schemas exist...")
        db_manager.ensure_schemas_exist(conn)

        print("Ensuring tables exist...")
        db_manager.ensure_tables_exist(conn)

        print("Generating synthetic data...")
        user_generator = UserProfileGenerator()
        users = user_generator.generate_user_profiles()

        data_inserter = DataInserter(conn)
        data_inserter.insert_user_data(users)
        data_inserter.insert_nutrition_log(users)

        conn.commit()
        print("Synthetic data inserted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()