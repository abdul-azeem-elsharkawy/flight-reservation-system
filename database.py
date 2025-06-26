import sqlite3     # importing sqlite3 module to work with SQLite database

# create a connection to the SQLite database
# if the database file does not exist, it will be created
# 'flights.db' is the name of the database file
connnect = sqlite3.connect('flights.db')

# create a cursor object using the connection
# the cursor is used to execute SQL commands
cursor = connnect.cursor()

# Create a table for storing flight information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        flight_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        date TEXT NOT NULL,
        seat_number TEXT NOT NULL
    )
''')

# save (commit) the changes to the database
# this is important to ensure that the table is created
connnect.commit()

# close the connection to the database
# this is important to free up resources and avoid database locks
connnect.close()
