import psycopg2
import random
import json
import requests
import os
import csv
from datetime import datetime, timedelta
from faker import Faker
from dotenv import load_dotenv
from search_foods_api import fetch_food_nutrition
from load_data_from_csv import load_food_items_from_csv, load_activity_types_from_csv


# load environment variables from .env
load_dotenv()

fake = Faker()


# database config from environment
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'health_fitness_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'placeholder_password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432)
}

# how many users to generate
# and how many days of data to generate
NUM_USERS = 2
DAYS = 2


def connect_db():
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


def ensure_schemas_exist(conn):
    """Ensure that all required schemas exist."""
    base_path = os.path.join(os.path.dirname(__file__), '../../sql/schemas/')
    execute_sql(conn, os.path.join(base_path, 'create_raw_schema.sql'))
    execute_sql(conn, os.path.join(base_path, 'create_staging_schema.sql'))
    execute_sql(conn, os.path.join(base_path, 'create_trusted_schema.sql'))


def ensure_tables_exist(conn):
    """Ensure that all required tables exist."""
    base_path = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/')
    execute_sql(conn, os.path.join(base_path, 'create_raw_user_data_table.sql'))
    execute_sql(conn, os.path.join(base_path, 'create_raw_nutrition_log_table.sql'))


def generate_user_profile(user_id=None):
    if user_id is None:
        user_id = random.randint(1, 1000000)

    return {
        'user_id': user_id,
        'name': fake.name(),
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


def generate_user_profiles():
    users = []
    for _ in range(NUM_USERS):
        profile = generate_user_profile(user_id=None)
        users.append(profile)
    return users


def insert_user_data(conn, users):
    sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_user_data.sql')
    activity_types = load_activity_types_from_csv('activity_types.csv')
    if not activity_types:
        print("No activity types found in the CSV file. Skipping user data insertion.")
        return

    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                # activity data
                activity_start = datetime.now() - timedelta(days=i)
                activity_type = random.choice(activity_types)
                steps = random.randint(1000, 25000)
                heart_rate = random.randint(60, 150)
                calories_burned = random.randint(150, 800)

                # sleep data
                sleep_start = datetime.now() - timedelta(hours=random.randint(0, 2))
                sleep_end = sleep_start + timedelta(hours=random.uniform(6.0, 9.0))
                sleep_quality_score = random.randint(50, 100)

                # goal data
                goal_type = random.choice(['calories burned', 'hours slept', 'steps taken'])
                if goal_type == 'calories burned':
                    goal_target = random.randint(150, 800)
                elif goal_type == 'hours slept':
                    goal_target = round(random.uniform(6.0, 9.0), 1)
                elif goal_type == 'steps taken':
                    goal_target = random.randint(1000, 25000)
                else:
                    goal_target = None

                crs.execute(load_sql(sql_file), (
                    user['user_id'], user['name'], user['age'], user['weight_kg'], user['height_cm'],
                    user['gender'], user['calorie_goal'], user['macro_goal'], activity_start, activity_type,
                    steps, heart_rate, calories_burned, sleep_start, sleep_end, sleep_quality_score, goal_type,
                    goal_target
                ))


def insert_nutrition_log(conn, users):
    sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_nutrition_log.sql')
    meals = ['breakfast', 'lunch', 'dinner', 'snack']
    food_items = load_food_items_from_csv('food_items_keywords.csv')
    if not food_items:
        print("No food items found in the CSV file. Skipping nutrition log insertion.")
        return

    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                for meal in meals:
                    food_item = random.choice(food_items)
                    nutrition = fetch_food_nutrition(food_item)
                    if nutrition:
                        crs.execute(load_sql(sql_file), (
                            user['user_id'], datetime.now().date() - timedelta(days=i),
                            nutrition['description'], meal,
                            nutrition['calories'], nutrition['carbs'],
                            nutrition['protein'], nutrition['fat']
                        ))
                    else:
                        print(f"Skipping {food_item} due to missing nutritional data.")


def run():
    conn = connect_db()
    try:
        print("Ensuring schemas exist...")
        ensure_schemas_exist(conn)

        print("Ensuring tables exist...")
        ensure_tables_exist(conn)

        print("Generating synthetic data...")
        users = generate_user_profiles()  
        insert_user_data(conn, users) 
        insert_nutrition_log(conn, users) 
        conn.commit()
        print("Synthetic data inserted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
