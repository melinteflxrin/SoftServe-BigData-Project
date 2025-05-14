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
    with conn.cursor() as crs:
        for _ in range(NUM_USERS):
            profile = generate_user_profile(user_id=None)
            crs.execute("""
                INSERT INTO raw.user_profile 
                (name, age, weight_kg, height_cm, gender, calorie_goal, macro_goal)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING user_id
            """, (
                profile['name'], profile['age'], profile['weight_kg'], profile['height_cm'],
                profile['gender'], profile['calorie_goal'], profile['macro_goal']
            ))
            new_user_id = crs.fetchone()[0]
            profile['user_id'] = new_user_id
            users.append(profile)
    return users

def insert_activity_log(conn, users):
    activity_types = load_activity_types_from_csv('activity_types.csv')  
    if not activity_types:
        print("No activity types found in the CSV file. Skipping activity log insertion.")
        return

    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                ts = datetime.now() - timedelta(days=i)
                activity = random.choice(activity_types)  
                crs.execute("""
                    INSERT INTO raw.activity_log 
                    (user_id, timestamp, activity_type, steps, heart_rate, calories_burned)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    user['user_id'], ts, activity,
                    random.randint(1000, 20000), random.randint(60, 150), random.randint(150, 800)
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
    meals = ['breakfast', 'lunch', 'dinner', 'snack']  # all possible meal types
    food_items = load_food_items_from_csv('food_items_keywords.csv')  # load food items from csv
    if not food_items:
        print("No food items found in the CSV file. Skipping nutrition log insertion.")
        return

    with conn.cursor() as crs:
        for user in users:
            for i in range(DAYS):
                for meal in meals:
                    food_item = random.choice(food_items)  # random food item from csv
                    nutrition = fetch_food_nutrition(food_item)  # get nutritional data from the API
                    if nutrition:  # insert if data is available
                        crs.execute("""
                            INSERT INTO raw.nutrition_log 
                            (user_id, date, food_item, meal_type, calories_per_100g, carbs_per_100g, protein_per_100g, fat_per_100g)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, (
                            user['user_id'], datetime.now().date() - timedelta(days=i),
                            nutrition['description'], meal,
                            nutrition['calories'], nutrition['carbs'],
                            nutrition['protein'], nutrition['fat']
                        ))
                    else:
                        print(f"Skipping {food_item} due to missing nutritional data.")

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
