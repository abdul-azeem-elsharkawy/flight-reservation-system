# ✈️ Flight Reservation System

A simple and elegant desktop application built with **Python** and **Tkinter**, allowing users to book, view, edit, and delete flight reservations — all stored locally using **SQLite**.

---

## 📸 Screenshots

> ![Home window](https://iili.io/FRFeEjn.png)

> ![Book a Flight window](https://iili.io/FRFeGQs.png)

> ![Reservation List window](https://iili.io/FRFeVCG.png)

> ![About window](https://iili.io/FRFeWGf.png)

---

## 🚀 Features

- 📋 Book flights with passenger details, seat number, and date
- 🗂️ View all reservations in a structured table
- ✏️ Edit existing reservations with confirmation
- ❌ Delete reservations with safety prompts
- 💾 Data stored in local SQLite database
- 📦 Convert to standalone `.exe` for Windows
- 🧭 Clean user interface with modern menus and icons

---

## 🛠️ Built With

- Python 3
- Tkinter (GUI)
- SQLite3 (Database)
- PyInstaller (for `.exe` packaging)

---

## 🖥️ How to Run the Project

### 🧪 Run from source (Python required):

1. Clone the repo:
    ```bash
   git clone https://github.com/abdul-azeem-elsharkawy/flight-reservation-system
   cd flight-reservation-system
    ````

2. Install required dependencies (if any):
    ```bash
   *(Standard Python installation is enough)*
    ````

3. Run the main file:
    ```bash
   python main.py
    ````

---

### 🧊 Run the standalone `.exe` (no Python needed):

1. Double-click on `Windows Apllication.exe`
2. Enjoy the app 🚀

---

## 📂 Project Structure

```
flight-reservation-system/
├── main.py                      # Main entry point (GUI home)
├── booking.py                   # Booking window
├── reservations.py              # View/Edit/Delete window
├── edit_reservation.py          # Edit popup window
├── database.py                  # SQLite setup
├── flights.db                   # Local database (auto-created)
├── airplane-ticket (icon).ico   # Application icon
├── README.md                    # Project documentation
├── LICENSE                      # Project License
```

---

## 📌 Notes

* Make sure `flights.db` and `airplane-ticket (icon).ico` exist in the same directory as `Windows Application.exe` when running standalone.
* The project is designed for educational/demo use and does not include user authentication or online integration.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
