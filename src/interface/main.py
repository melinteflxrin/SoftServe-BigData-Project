import tkinter as tk
from tkinter import messagebox
from ui_components import create_labeled_entry
from utils import run_etl_and_dashboard

def on_run():
    """
    collects user input from the GUI, runs the ETL and dashboard scripts,
    and displays a message box with the result.
    """
    try:
        num_users = int(entries['Number of Users'].get())
        num_days = int(entries['Number of Days'].get())
        db_host = entries['DB Host'].get()
        db_port = entries['DB Port'].get()
        db_user = entries['DB User'].get()
        db_pass = entries['DB Password'].get()
        db_name = entries['DB Name'].get()
        usda_api_key = entries['USDA API Key'].get()
        run_etl_and_dashboard(num_users, num_days, db_host, db_port, db_user, db_pass, db_name, usda_api_key)
        messagebox.showinfo("Success", "Scripts ran and dashboards generated!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Health Fitness Data Pipeline")

fields = [
    "Number of Users", "Number of Days", "DB Host", "DB Port",
    "DB User", "DB Password", "DB Name", "USDA API Key"
]
entries = {}

for idx, field in enumerate(fields):
    """
    create labeled entry fields for each required input in the GUI.
    """
    entries[field] = create_labeled_entry(root, field, idx)

run_button = tk.Button(root, text="Run Pipeline", command=on_run)
run_button.grid(row=len(fields), column=1, pady=10)

root.mainloop()