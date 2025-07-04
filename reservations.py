import tkinter as tk
from tkinter import ttk
import sqlite3
import os
import edit_reservation # Import the edit_reservation.py module to handle editing reservations 

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

    # Add Edit Selected button to edit the selected reservation
    # This button will open the edit_reservation window with the selected reservation data
    edit_button = ttk.Button(window, text="Edit Selected", command=lambda: open_edit())
    edit_button.pack(pady=5)

    # add Delete Selected button to delete the selected reservation
    # This button will delete the selected reservation from the database and refresh the Treeview
    delete_button = ttk.Button(window, text="Delete Selected", command=lambda: delete_selected())
    delete_button.pack(pady=5)

    # Function to open the edit window with the selected reservation data
    # This function will be called when the user clicks on the Edit Selected button
    def open_edit():
        selected = tree.focus()  # Get the id of currently selected reservation in the Treeview
        if not selected:
            tk.messagebox.showerror("No Selection", "Please select a reservation to edit.")
            return
        
        data = tree.item(selected)["values"] # Get the data of the selected reservation
        if data:
            edit_reservation.open_edit_window(data, refresh_tree) 

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
    
      
    # Refresh function to reload the data from the database
    # This function will be called when the user edits a reservation
    def refresh_tree():
        for row in tree.get_children():
            tree.delete(row)   # Clear the current data in the Treeview

        # Fetch new data from the database
        try:
            connect = sqlite3.connect("flights.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM reservations")
            rows = cursor.fetchall()
            connect.close()
            for row in rows:
                tree.insert("", "end", values=row)  # Insert the new data into the Treeview

        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to reload data: {e}")

    # function to delete the selected reservation from the database
    # This function will be called when the user clicks on the Delete Selected button
    def delete_selected():
        selected = tree.focus()
        if not selected:
            tk.messagebox.showerror("No Selection", "Please select a reservation to delete.")
            return

        data = tree.item(selected)["values"]
        if not data:
            return

        confirm = tk.messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete reservation for '{data[1]}'?")
        if not confirm:
            return

        try:
            connect = sqlite3.connect("flights.db")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM reservations WHERE id = ?", (data[0],))
            connect.commit()
            connect.close()

            tk.messagebox.showinfo("Deleted", "Reservation deleted successfully.")
            refresh_tree()

        except Exception as e:
            tk.messagebox.showerror("Database Error", f"An error occurred while deleting:\n{e}")