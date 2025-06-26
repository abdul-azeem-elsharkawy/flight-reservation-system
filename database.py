import sqlite3

# إنشاء اتصال بقاعدة البيانات (أو إنشاؤها لو مش موجودة)
connnect = sqlite3.connect('flights.db')

# إنشاء كائن cursor للتعامل مع قاعدة البيانات
cursor = connnect.cursor()

# إنشاء جدول الحجوزات لو مش موجود
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

# حفظ التغييرات
connnect.commit()

# إغلاق الاتصال
connnect.close()
