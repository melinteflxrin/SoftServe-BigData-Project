import psycopg2
import random
import json
from datetime import datetime, timedelta
from faker import Faker
from dotenv import load_dotenv
import os

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

NUM_USERS = 10
DAYS = 7

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def generate_user_profile(user_id):
    return {
        'user_id': user_id,
        'name': fake.name(),
        'age': random.randint(18, 60),
        'weight': round(random.uniform(55, 100), 1),
        'height': round(random.uniform(150, 200), 1),
        'gender': random.choice(['Male', 'Female']),
        'calorie_goal': random.choice([1800, 2000, 2200]),
        'macro_goal': json.dumps({
            'carbs': random.randint(200, 300),
            'protein': random.randint(50, 150),
            'fat': random.randint(40, 80)
        })
    }

def insert_user_profiles(conn):
    users = [generate_user_profile(i + 1) for i in range(NUM_USERS)]
    with conn.cursor() as crs:
        for u in users:
            crs.execute("""
                INSERT INTO raw.user_profile 
                (user_id, name, age, weight, height, gender, calorie_goal, macro_goal)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                u['user_id'], u['name'], u['age'], u['weight'], u['height'],
                u['gender'], u['calorie_goal'], u['macro_goal']
            ))
    return users

def insert_activity_log(conn, users):
    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                ts = datetime.now() - timedelta(days=i)
                crs.execute("""
                    INSERT INTO raw.activity_log 
                    (user_id, timestamp, activity_type, steps, heart_rate, calories_burned)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    user['user_id'], ts, random.choice(['walking', 'running']),
                    random.randint(2000, 10000), random.randint(60, 150), random.randint(150, 800)
                ))

def insert_sleep_log(conn, users):
    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                sleep_start = datetime.now() - timedelta(days=i, hours=random.randint(0, 2))
                sleep_end = sleep_start + timedelta(hours=random.uniform(6.0, 9.0))
                crs.execute("""
                    INSERT INTO raw.sleep_log 
                    (user_id, date, sleep_start, sleep_end, sleep_quality_score)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    user['user_id'], sleep_start.date(), sleep_start, sleep_end,
                    random.randint(50, 100)
                ))

def insert_nutrition_log(conn, users):
    meals = ['breakfast', 'lunch', 'dinner', 'snack']
    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                for meal in meals:
                    crs.execute("""
                        INSERT INTO raw.nutrition_log 
                        (user_id, date, food_item, meal_type, calories, carbs, protein, fat)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        user['user_id'], datetime.now().date() - timedelta(days=i),
                        fake.word(), meal,
                        random.randint(100, 600),
                        random.randint(10, 70),
                        random.randint(5, 40),
                        random.randint(5, 30)
                    ))

def insert_goals_log(conn, users):
    goal_types = ['activity', 'sleep', 'nutrition']
    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                for goal in goal_types:
                    target = random.randint(100, 1000)
                    actual = target + random.randint(-200, 200)
                    status = 'met' if actual >= target else 'not met'
                    crs.execute("""
                        INSERT INTO raw.goals_log 
                        (user_id, date, goal_type, target_value, actual_value, status)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        user['user_id'], datetime.now().date() - timedelta(days=i),
                        goal, target, actual, status
                    ))

def run():
    conn = connect_db()
    try:
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