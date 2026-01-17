import time

from LearningSystem.learning_system_project.constants.messages import get_email_text, get_password_text


def print_messages(func_name: str) -> None:
    """
    This function is being called from many others.
    Its purpose is to different print messages to the User,
    depending on the function which have called it.
    """
    message = ''

    if func_name == "get_email":
        message = get_email_text

    elif func_name == "get_password":
        message = get_password_text

    print(message)


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


# Messaging
def handle_invalid_input(some_input: str):
    """
    Returns an error message every time it is called
    :param some_input: string
    :return: str
    """
    return f'Error: {some_input} is an invalid input\n'


def authentication_failure():
    print("Authentication failed!")
    raise SystemExit
