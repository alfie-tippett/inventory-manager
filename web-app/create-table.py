import sqlite3

def create_table():
    conn = sqlite3.connect("inventory.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS inventory
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    model TEXT,
                    serial_num TEXT,
                    condition TEXT)''')
    conn.commit()
    conn.close()


create_table()