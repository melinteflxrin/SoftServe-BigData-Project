import os
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

class Dashboard:
    SQL_VIEW_FILES = [
        '../../sql/business_view/create_view_pct_users_achieved_goals.sql',
        '../../sql/business_view/create_view_user_favourite_food.sql',
        '../../sql/business_view/create_view_avg_calories_burned.sql',
        '../../sql/business_view/create_view_user_avg_macros.sql'
    ]

    def __init__(self):
        """initialize Dashboard and connect to database."""
        load_dotenv()
        self.db_config = {
            'dbname': os.getenv('DB_NAME', 'health_fitness_db'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', 'placeholder_password'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', 5432)
        }
        self.conn = psycopg2.connect(**self.db_config)

    def __del__(self):
        "close database connection on object deletion."""
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()

    def execute_sql_file(self, file_path):
        """execute SQL file to create a database view."""
        with open(file_path, 'r') as f:
            sql = f.read()
        with self.conn.cursor() as cur:
            cur.execute(sql)
        self.conn.commit()
        print(f"Executed {file_path}")

    def create_views(self):
        """create all necessary SQL views for the dashboard."""
        base_path = os.path.dirname(__file__)
        for sql_file in self.SQL_VIEW_FILES:
            full_path = os.path.join(base_path, sql_file)
            self.execute_sql_file(full_path)

    def fetch_dataframe(self, query):
        """fetch a pandas DataFrame from SQL query."""
        return pd.read_sql_query(query, self.conn)

    def plot_pct_users_achieved_goals(self, ax):
        """plot the percentage of users who achieved their goals."""
        df = self.fetch_dataframe("SELECT * FROM trusted.vw_pct_users_achieved_goals")
        ax.bar(['Achieved Goals'], df['pct_users_achieved_goals'])
        ax.set_title('% of Users Achieved Goals')
        ax.set_ylabel('% Achieved')

    def plot_user_favourite_food(self, ax):
        """plot the most popular favourite food for users."""
        df = self.fetch_dataframe("SELECT * FROM trusted.vw_user_favourite_food")
        fav_counts = df['favourite_food'].value_counts()
        fav_counts.plot(kind='bar', ax=ax)
        ax.set_title("Most Popular Favourite Foods")
        ax.set_ylabel('Number of Users')
        ax.set_xlabel('Food')

    def plot_user_daily_avg_calories_burned(self, ax):
        """plot the average daily calories burned per user."""
        df = self.fetch_dataframe("SELECT * FROM trusted.vw_user_daily_avg_calories_burned")
        df.plot.bar(x='user_name', y='avg_calories_burned', legend=False, ax=ax)
        ax.set_title('Avg Calories Burned Per User')
        ax.set_ylabel('Avg Calories Burned')
        ax.set_xlabel('User')

    def plot_user_avg_macros(self, ax):
        """plot the average macronutrient distribution per user."""
        df = self.fetch_dataframe("SELECT * FROM trusted.vw_user_avg_macros")
        df.set_index('user_name')[['avg_carbs_per_100g', 'avg_protein_per_100g', 'avg_fat_per_100g']].plot.bar(ax=ax)
        ax.set_title('Average Macronutrient Distribution Per User')
        ax.set_ylabel('Average per 100g')
        ax.set_xlabel('User')

    def show_dashboards(self):
        """create views and display the dashboard with all plots."""
        self.create_views()
        fig, axs = plt.subplots(2, 2, figsize=(16, 10))
        fig.canvas.manager.set_window_title("Health & Fitness Analytics Dashboard")
        self.plot_pct_users_achieved_goals(axs[0, 0])
        self.plot_user_favourite_food(axs[0, 1])
        self.plot_user_daily_avg_calories_burned(axs[1, 0])
        self.plot_user_avg_macros(axs[1, 1])
        plt.tight_layout()
        plt.show()

def main():
    dashboard = Dashboard()
    dashboard.show_dashboards()

if __name__ == "__main__":
    main()