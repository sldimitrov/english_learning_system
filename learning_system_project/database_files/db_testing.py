import sqlite3
import hashlib


def register_user(name, user_password) -> bool:
    # Connect to the database
    conn = sqlite3.connect("userdata2.db")
    cur = conn.cursor()

    # Add a column to the table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata2 (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)

    # Parse the username and password into bytes
    username, password = name, hashlib.sha256(user_password.encode()).hexdigest()

    # Insert data into the database
    cur.execute("INSERT INTO userdata2 (username, password) VALUES (?, ?)", (username, password))

    # Commit the changes
    conn.commit()

    return True


def login_user() -> None:
    # Get input from the user - insert functions here
    name = input('Please, enter your email: ')
    user_password = input('Password: ')

    # encrypt password and etc...
    username, password = name, hashlib.sha256(user_password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect("userdata2.db")
    cur = conn.cursor()

    # Find if there is a match within the database with username, pass
    cur.execute("SELECT * FROM userdata2 WHERE username = ? AND password = ?", (username, password))

    # If there is a match
    if cur.fetchall():
        print("Login successful!")
        # secrets
        # services
    else:  # if there is no match
        print("Login failed!")


def is_email_used(email):
    # Connect to the database
    conn = sqlite3.connect("userdata2.db")
    cur = conn.cursor()

    # Find if there is a match within the database with username, pass
    cur.execute("SELECT username FROM userdata2 WHERE username = ?", email)

    # If there is a match
    if cur.fetchall():
        print("Email is used!")
    else:
        print("Email is not used!")


# is_email_used(input('Enter email: '))

# Read User input
command = input("reg or log: ")

# In case he doesn't exist in the database
if command == "reg":
    # Read User data
    user_name = input('name: ')
    user_pass = input('pass: ')

    if register_user(user_name, user_pass):
        print("User was registered.")

# In case he is already in the database
elif command == "log":
    login_user()


else:
    print(f"Unknown command {command}")
