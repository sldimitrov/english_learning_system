# Messaging
from LearningSystem.learning_system_project.auth.validators import is_email_valid
from LearningSystem.learning_system_project.constants.constants import valid_answers
from LearningSystem.learning_system_project.messaging.printer import handle_invalid_input, print_messages


def get_input() -> str:
    """
    When called: This function prints out a message, which asks the user to input a single number.
    Then: Checks if user's input is valid by calling the (input validator) function and if it's not -
    calls out the (handle invalid input) which prints out an error message.
    :return: str
    """
    while True:
        choice = input('\nChoose operation from (1/2/3/4/5/6/7) or (m) if you want to see the menu: ')
        if choice is input_validator(choice):
            print(handle_invalid_input(choice))
        else:
            return choice


# Messaging
def input_validator(message: str):
    """
    This functions checks if the choice of the user occurs in the valid list of answers
    If not: the (handle invalid input) func. is being called.
    :param message: string
    :return: str / bool
    """
    if message not in valid_answers:
        message = handle_invalid_input(message)
        return message
    return True


# Messaging
def get_email():
    """
    This function is being called by the main in order to get
    the email address of the user.
    It also calls the 1-(print_messages) and the 2-(is_email_valid) functions
    The first one prints out the email validation rules.
    If the second one returns true, the function returns the email to the main.
    """

    while True:
        print_messages(get_email.__name__)
        user_email = input("Enter an email address, please: ")
        is_valid_email = is_email_valid(user_email)
        if is_valid_email:
            return user_email
