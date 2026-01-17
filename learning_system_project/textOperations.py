import constants
import time
from constants.messages import origin_story, menu_options, get_email, get_password, ending_message

# Enable skip by pressing any key
def greet_user():
    print("Hello, Dear User!")
    time.sleep(0.8)
    print("Welcome to my application!")
    time.sleep(1.6)
    print("\nLearning foreign languages can give you the wings to conquer the world.")
    print("Are you ready to sink in a world fulfilled with many wonders and knowledge? ")
    time.sleep(5)
    print("\nLets get into it...")
    time.sleep(0.6)

def print_messages(func_name: str) -> None:
    """
    This function is being called from many others.
    Its purpose is to different print messages to the User,
    depending on the function which have called it.
    """
    message = ''

    if func_name == "get_email":
        message = get_email

    elif func_name == "get_password":
        message = get_password

    print(message)
