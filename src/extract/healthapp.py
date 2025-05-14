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
NUM_USERS = 10
DAYS = 7

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
    execute_sql(conn, os.path.join(base_path, 'create_raw_user_profile_table.sql'))
    execute_sql(conn, os.path.join(base_path, 'create_raw_activity_log_table.sql'))
    execute_sql(conn, os.path.join(base_path, 'create_raw_sleep_log_table.sql'))
    execute_sql(conn, os.path.join(base_path, 'create_raw_nutrition_log_table.sql'))
    execute_sql(conn, os.path.join(base_path, 'create_raw_goals_log_table.sql'))

def generate_user_profile(user_id=None):
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

def insert_user_profiles(conn):
    users = []
    sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_user_profile.sql')
    with conn.cursor() as crs:
        for _ in range(NUM_USERS):
            profile = generate_user_profile(user_id=None)
            crs.execute(load_sql(sql_file), (
                profile['name'], profile['age'], profile['weight_kg'], profile['height_cm'],
                profile['gender'], profile['calorie_goal'], profile['macro_goal']
            ))
            new_user_id = crs.fetchone()[0]
            profile['user_id'] = new_user_id
            users.append(profile)
    return users

def insert_activity_log(conn, users):
    sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_activity_log.sql')
    activity_types = load_activity_types_from_csv('activity_types.csv')
    if not activity_types:
        print("No activity types found in the CSV file. Skipping activity log insertion.")
        return

    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                ts = datetime.now() - timedelta(days=i)
                activity = random.choice(activity_types)
                crs.execute(load_sql(sql_file), (
                    user['user_id'], ts, activity,
                    random.randint(1000, 20000), random.randint(60, 150), random.randint(150, 800)
                ))

def insert_sleep_log(conn, users):
    sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_sleep_log.sql')
    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                sleep_start = datetime.now() - timedelta(days=i, hours=random.randint(0, 2))
                sleep_end = sleep_start + timedelta(hours=random.uniform(6.0, 9.0))
                crs.execute(load_sql(sql_file), (
                    user['user_id'], sleep_start.date(), sleep_start, sleep_end,
                    random.randint(50, 100)
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

def insert_goals_log(conn, users):
    sql_file = os.path.join(os.path.dirname(__file__), '../../sql/tables/raw/insert_raw_goals_log.sql')
    goal_types = ['activity', 'sleep', 'nutrition']
    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                for goal in goal_types:
                    target = random.randint(100, 1000)
                    actual = target + random.randint(-200, 200)
                    status = 'met' if actual >= target else 'not met'
                    crs.execute(load_sql(sql_file), (
                        user['user_id'], datetime.now().date() - timedelta(days=i),
                        goal, target, actual, status
                    ))

def run():
    conn = connect_db()
    try:
        print("Ensuring schemas exist...")
        ensure_schemas_exist(conn)

        print("Ensuring tables exist...")
        ensure_tables_exist(conn)

        print("Generating synthetic data...")
        users = insert_user_profiles(conn)
        insert_activity_log(conn, users)
        insert_sleep_log(conn, users)
        insert_nutrition_log(conn, users)
        insert_goals_log(conn, users)
        conn.commit()
        print("Synthetic data inserted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
