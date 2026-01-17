# Auth
import hashlib
import sqlite3

from LearningSystem.learning_system_project.auth.validators import is_password_valid
from LearningSystem.learning_system_project.messaging.printer import print_messages
from LearningSystem.learning_system_project.messaging.prompts import get_email


def register_user() -> bool:
    """
    This functions take no params. It calls 2 other functions in order to validate the User's input.
    After that register the user into the database by simply adding its email and encrypted password.
    It returns bool after all.
    """
    # Read data from the User
    email = get_email()
    user_password = get_password()

    # Connect to the database
    conn = sqlite3.connect("userdata2.db")
    cur = conn.cursor()

    # Add a row to the table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata2 (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)

    # Parse the username and password into bytes
    email, password = email, hashlib.sha256(user_password.encode()).hexdigest()

    # Insert data into the database
    cur.execute("INSERT INTO userdata2 (username, password) VALUES (?, ?)", (email, password))

    # Commit the changes
    conn.commit()

    return True

# Auth
def login_user() -> bool:
    """
    This functions take and return no parameters.
    It takes User input and check for matches in the database.
    If there is a match - give access to the User
    """
    # Get input from the user - insert functions here
    print("\nPlease input login info.")
    email = input("Your email address: ")
    user_password = input("Your password: ")

    # encrypt password and etc...
    email, password = email, hashlib.sha256(user_password.encode()).hexdigest()

    # Connect to the database
    conn = sqlite3.connect("userdata2.db")
    cur = conn.cursor()

    # Find if there is a match within the database with username, pass
    cur.execute("SELECT * FROM userdata2 WHERE username = ? AND password = ?", (email, password))

    # If there is a match
    if cur.fetchall():
        return True
        # secrets
        # services
    else:  # if there is no match
        print("There is no user with such credentials in the database.")
        return False


def get_password():
    """
    This function is being called by the main in order to get
    the password of the user.

    If the password is valid, we ask the User to repeat
    his password in the console.

    If the User pass the authentication we return the password to the main
    """
    while True:
        # Read User password
        print_messages(get_password.__name__)

        while 1:
            user_password = input("Create a password: ")
            output_message = is_password_valid(user_password)
            if output_message == "":
                counter = 3
                while True:
                    repeated_password = input('Enter the same password: ')
                    if user_password == repeated_password:
                        return user_password
                    else:
                        counter -= 1
                        if counter <= 0:
                            print(f'\nUnfortunately you failed to repeat your password. Try again with new one!')
                            break
                        print('\nIncorrect try to repeat your password!')
                        print(f'{counter} tries left.' if counter > 1 else f'{counter} try left.')
                        continue
            else:
                print(output_message)
