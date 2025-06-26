import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

def open_edit_window(data, refresh_callback):
    # data عبارة عن tuple: (id, name, flight_number, departure, destination, date, seat_number)
    edit_win = tk.Toplevel()
    edit_win.title("Edit Reservation")
    edit_win.geometry("400x400")
    edit_win.resizable(False, False)
    edit_win.configure(bg="#f9fbfc")

    # add an icon to the window
    if os.path.exists("airplane-ticket (icon).ico"):
        # If the icon file exists, set it as the window icon
        edit_win.iconbitmap("airplane-ticket (icon).ico")

    labels = ["Passenger Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
    fields = {}

    for idx, label_text in enumerate(labels):
        label = ttk.Label(edit_win, text=label_text)
        label.pack(pady=(10 if idx == 0 else 5, 0))
        entry = ttk.Entry(edit_win, width=40)
        entry.insert(0, data[idx + 1])  # +1 لأن data[0] هو الـ ID
        entry.pack(pady=2)
        fields[label_text] = entry

    def update_reservation():
        new_data = [entry.get().strip() for entry in fields.values()]
        if not all(new_data):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            conn = sqlite3.connect("flights.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE reservations
                SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                WHERE id = ?
            """, (*new_data, data[0]))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Reservation updated successfully!")
            edit_win.destroy()
            refresh_callback()  # إعادة تحميل البيانات من القاعدة
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    # زر الحفظ
    save_button = ttk.Button(edit_win, text="Save Changes", command=update_reservation)
    save_button.pack(pady=20)
