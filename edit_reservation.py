import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# Create a new window for editing reservations
# This function will be invoked when the user selects a reservation to edit
def open_edit_window(data, refresh_callback):
    edit_win = tk.Toplevel()
    edit_win.title("Edit Reservation")
    edit_win.geometry("400x450") 
    edit_win.resizable(False, False)
    edit_win.configure(bg="#f9fbfc")

    # add an icon to the window
    if os.path.exists("airplane-ticket (icon).ico"):
        # If the icon file exists, set it as the window icon
        edit_win.iconbitmap("airplane-ticket (icon).ico")

    # Fields dictionary to hold the entry widgets and their labels
    labels = ["ID", "Passenger Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
    fields = {} # Dictionary to hold the labels and entry fields

    # Create labels and entry fields for each piece of data
    for idx, label_text in enumerate(labels):
        label = ttk.Label(edit_win, text=label_text)
        label.pack(pady=(10 if idx == 0 else 5, 0))
        entry = ttk.Entry(edit_win, width=40)  
        entry.insert(0, data[idx])  # Insert old data so the user can see it and edit it
        
        if label_text in ["ID", "Passenger Name"]:
            entry.config(state='readonly')  # Make ID and Passenger Name visible but not editable

        entry.pack(pady=2)
        fields[label_text] = entry

    # Function to update the reservation in the database
    # This function will be called when the user clicks the Save Changes button
    def update_reservation():
        new_data = [entry.get().strip() for entry in list(fields.values())[2:]] # New values from user input (from Flight Number to Seat Number)

        if not all(new_data): # Check if all fields are filled
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            connect = sqlite3.connect("flights.db")
            cursor = connect.cursor()
            cursor.execute("""
                UPDATE reservations
                SET flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                WHERE id = ?
            """, (*new_data, data[0]))  # Use the ID from the original data to update the correct record & *new_data unpacks the list into separate arguments to put them instead of ? in the database
            connect.commit()
            connect.close()

            messagebox.showinfo("Success", "Reservation updated successfully!")
            edit_win.destroy()
            refresh_callback()  # Call the refresh function to update the reservations list in the reservations window

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    # Adding a Save Changes button to save changes
    save_button = ttk.Button(edit_win, text="Save Changes", command=update_reservation)
    save_button.pack(pady=20)