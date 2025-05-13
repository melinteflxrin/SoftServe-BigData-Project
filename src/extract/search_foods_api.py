import os
import requests
from dotenv import load_dotenv
import csv

load_dotenv()

def fetch_food_nutrition(food_item):
    """Fetch nutritional data for a food item using the USDA FoodData Central API."""
    USDA_API_KEY = os.getenv('USDA_API_KEY')
    if not USDA_API_KEY:
        print("USDA API key is missing. Please check your .env file.")
        return None

    url = f"https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {
        'query': food_item,
        'pageSize': 1,  # limit to 1 result
        'api_key': USDA_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'foods' in data and len(data['foods']) > 0:
                food = data['foods'][0]  # the first food result
                print(f"Nutritional data for '{food_item}':")
                print(f"Description: {food.get('description', 'N/A')}")

                # extract specific nutrients by name
                nutrients = {n['nutrientName']: n for n in food.get('foodNutrients', [])}
                calories = nutrients.get('Energy', {}).get('value', 'N/A')
                carbs = nutrients.get('Carbohydrate, by difference', {}).get('value', 'N/A')
                protein = nutrients.get('Protein', {}).get('value', 'N/A')
                fat = nutrients.get('Total lipid (fat)', {}).get('value', 'N/A')

                # return the extracted values as a dictionary
                return {
                    'description': food.get('description', 'N/A'),
                    'calories': calories,
                    'carbs': carbs,
                    'protein': protein,
                    'fat': fat
                }
            else:
                print(f"No nutritional data found for '{food_item}'.")
                return None
        else:
            print(f"Failed to fetch data from USDA API. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"Error while calling USDA API: {e}")
        return None


def load_food_items_from_csv(file_name):
    """Load food items from a CSV file."""
    # get directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    food_items = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                food_items.append(row['food_item'])
    except Exception as e:
        print(f"Error reading food items from CSV: {e}")
    return food_items   