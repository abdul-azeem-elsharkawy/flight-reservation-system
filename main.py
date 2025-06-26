import tkinter as tk
from tkinter import ttk
import database  # importing the database.py module
import booking  # importing the booking.py module
import os

# create the main application window
root = tk.Tk()
root.title("Flight Reservation System")
root.geometry("400x300")  # window size
root.configure(bg="#f0f4f7") # set background color
root.resizable(False, False)  # prevent resizing

# add an icon to the window
if os.path.exists("airplane-ticket (icon).ico"):
    # If the icon file exists, set it as the window icon
    root.iconbitmap("airplane-ticket (icon).ico")

# This label will be used to display the title of the application
title_label = ttk.Label(root, text="Welcome to Flight Reservation System", font=("Helvetica", 14, "bold"))
title_label.pack(pady=30)

# button to book a flight
# This button will be linked to the booking functionality later
book_button = ttk.Button(root, text="Book Flight", command=booking.open_booking_window)  # invoking the open_booking_window function from booking.py
book_button.pack(pady=10)

# button to view reservations
# This button will be linked to the view reservations functionality later
view_button = ttk.Button(root, text="View Reservations")
view_button.pack(pady=10)

# This will keep the application running and responsive to user input
root.mainloop()