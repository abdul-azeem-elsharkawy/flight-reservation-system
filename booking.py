import tkinter as tk
from tkinter import ttk, messagebox  # messagebox for message boxes like success and failed
import sqlite3
import os

# create a new window for booking flights
# we will invoke this function when the user clicks on the "Book Flight" button
def open_booking_window():
    booking_win = tk.Toplevel()
    booking_win.title("Book a Flight")
    booking_win.geometry("400x400")
    booking_win.resizable(False, False)
    booking_win.configure(bg="#f9fbfc")

    # add an icon to the window
    if os.path.exists("airplane-ticket (icon).ico"):
        # If the icon file exists, set it as the window icon
        booking_win.iconbitmap("airplane-ticket (icon).ico")

    # Fields for flight booking that the user needs to fill
    fields = {
        "Passenger Name": None,
        "Flight Number": None,
        "Departure": None,
        "Destination": None,
        "Date (YYYY-MM-DD)": None,
        "Seat Number": None
    }

    # Store the entry widgets in a dictionary for easy access
    # This will allow us to retrieve the user input when saving the reservation
    entries = {}

    for idx, (label_text, _) in enumerate(fields.items()):
        label = ttk.Label(booking_win, text=label_text)
        label.pack(pady=(10 if idx == 0 else 5, 0))
        entry = ttk.Entry(booking_win, width=40)  # Create an entry widget for each field to allow user input
        entry.pack(pady=2)
        entries[label_text] = entry

    # Function to save the reservation to the database
    # This function will be called when the user clicks on the "Save Reservation" button
    def save_reservation():
        data = [entry.get().strip() for entry in entries.values()]
        
        # Check if all fields are filled
        # If any field is empty, show an error message and return
        if not all(data):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            connect = sqlite3.connect("flights.db")
            cursor = connect.cursor()
            cursor.execute("""
                INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                VALUES (?, ?, ?, ?, ?, ?)
            """, data) # Insert the data into the reservations table
                        # ? are to prevent SQL injection attacks
            connect.commit()
            connect.close()
            messagebox.showinfo("Success", "Flight booked successfully!")
            booking_win.destroy()
        
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}") # Show an error message if there is a database error

    # create "Save Reservation" button to save the reservation
    # This button will call the save_reservation function when clicked
    save_button = ttk.Button(booking_win, text="Save Reservation", command=save_reservation)
    save_button.pack(pady=20)
