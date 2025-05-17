import tkinter as tk

def create_labeled_entry(root, label, row):
    """
    create a labeled entry field in Tkinter window
    """
    tk.Label(root, text=label).grid(row=row, column=0, sticky='e', padx=5, pady=5)
    entry = tk.Entry(root, show="*" if "Password" in label else "")
    entry.grid(row=row, column=1, padx=5, pady=5)
    return entry