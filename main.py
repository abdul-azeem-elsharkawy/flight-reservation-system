import tkinter as tk
from tkinter import ttk
import database  # importing the database.py module
import booking  # importing the booking.py module
import reservations  # importing the reservations.py module
import os
import webbrowser  # for opening the GitHub repository in a web browser

# create the main application window
root = tk.Tk()
root.title("Flight Reservation System")
root.geometry("400x300")  # window size
root.configure(bg="#f0f4f7") # set background color
root.resizable(False, False)  # prevent resizing

# Create a menu bar
menubar = tk.Menu(root)
# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: show_about())
help_menu.add_command(label="Visit GitHub Repo", command=lambda: open_github())
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

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
view_button = ttk.Button(root, text="View Reservations", command=reservations.open_reservations_window)  # invoking the open_reservations_window function from reservations.py
view_button.pack(pady=10)

# Confirmation dialog for closing the application
# This function will be called when the user tries to close the application window
def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you really want to exit the application?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Function to show the About dialog
def show_about():
    tk.messagebox.showinfo(
        "About",
        "✈️ Flight Reservation System\n"
        "Version 1.0\n"
        "Developed by Abdul-Azeem Lotfy El-Sharkawy\n\n"
        "This application allows users to:\n"
        "• Book flights\n"
        "• View, edit, and delete reservations\n\n"
        "For more information, visit the GitHub repository."
    )


# function to open GitHub repository
def open_github():
    webbrowser.open("https://github.com/abdul-azeem-elsharkawy/flight-reservation-system")

# This will keep the application running and responsive to user input
root.mainloop()
