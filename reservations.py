import tkinter as tk
from tkinter import ttk
import sqlite3
import os

# create a new window for displaying reservations
# we will invoke this function when the user clicks on the "View Reservations" button
def open_reservations_window():
    window = tk.Toplevel()
    window.title("Reservations List")
    window.geometry("800x400")
    window.resizable(False, False)

    # add an icon to the window
    if os.path.exists("airplane-ticket (icon).ico"):
        # If the icon file exists, set it as the window icon
        window.iconbitmap("airplane-ticket (icon).ico")

    # This label will be used to display the title of the reservations window
    label = ttk.Label(window, text="All Flight Reservations", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    # Create a Treeview widget to display the reservations in form of a table
    columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
    tree = ttk.Treeview(window, columns=columns, show="headings")  # show="headings" means we only show our columns

    # Set up the headings and columns for the Treeview
    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())
        tree.column(col, width=100, anchor="center")

    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Load data from the database and insert it into the Treeview
    try:
        connect = sqlite3.connect("flights.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM reservations")
        rows = cursor.fetchall()
        connect.close()

        for row in rows:
            tree.insert("", "end", values=row)

    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred while loading data:\n{e}")