import sqlite3

bold_start = '\033[1m'
bold_end   = '\033[0m'

# def create_table():
#     conn = sqlite3.connect("inventory.db")
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS inventory
#                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     model TEXT,
#                     serial_num TEXT,
#                     condition TEXT)''')
#     conn.commit()
#     conn.close()

def home():
    print("\n\n")
    print("################################")
    print("          JJFAB Retros          ")
    print("      Inventory Management      ")
    print("################################\n")
    print("Welcome to JJFAB Retros Inventory Management, \nPlease select what you would like to do today: ")
    user_choice = int(input("1. View Inventory\n2. Add Stock\n3. Remove Stock\n\nEnter your option here: "))

    while user_choice not in range (1,4):
        print(bold_start, "\n~~ Please enter an option from 1-3! ~~\n ", bold_end)
        user_choice = int(input("1. View Inventory\n2. Add Stock\n3. Remove Stock\n\nEnter your option here: "))

    if user_choice == 1:
        view_inventory()
    elif user_choice == 2:
        add_stock()
    elif user_choice == 3:
        remove_stock()
    else:
        print(bold_start, "~~ Error has occured ~~", bold_end)

def view_inventory():
    try:
        db_connect = sqlite3.connect('inventory.db')
        db_conn = db_connect.cursor()
        db_conn.execute("SELECT * FROM inventory")
        inventory = db_conn.fetchall()
        db_connect.close()
        print(inventory, "\n")
    except sqlite3.Error as e:
            print(f"Database error: {e}")
    home()
    

def add_stock():
    model = input("Please enter the model: ")
    serial_num = input("Please enter the Serial Number: ")
    condition = input("Please enter the condition: ")
    try:
        db_connect = sqlite3.connect('inventory.db')
        db_conn = db_connect.cursor()
        db_conn.execute("INSERT INTO inventory (model, serial_num, condition) VALUES (?, ?, ?)", (model, serial_num, condition))
        db_connect.commit()
        print("Item inserted succesfully!")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    home()

def remove_stock():
    inventory_id = int(input("Please enter the ID of the item you want to delete: "))
    try:
        db_connect = sqlite3.connect('inventory.db')
        db_conn = db_connect.cursor()

        db_conn.execute("DELETE FROM inventory WHERE id = ?", (inventory_id,))
        db_connect.commit()
        db_connect.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    home()

home()


