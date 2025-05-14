import csv
import os
import requests

# get directory of current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')  # adjust path to 'data' folder

def load_food_items_from_csv(file_name):
    """Load food items from a CSV file."""
    food_items = []
    file_path = os.path.join(DATA_DIR, file_name) 
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                food_items.append(row['food_item'])
    except Exception as e:
        print(f"Error reading food items from CSV: {e}")
    return food_items


def load_activity_types_from_csv(file_name):
    """Load activity types from a CSV file."""
    activity_types = []
    file_path = os.path.join(DATA_DIR, file_name) 
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                activity_types.append(row['activity_type'])
    except Exception as e:
        print(f"Error reading activity types from CSV: {e}")
    return activity_types