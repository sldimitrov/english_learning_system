# Auth - Validation
import sqlite3
import string

from LearningSystem.learning_system_project import Exceptions
from LearningSystem.learning_system_project.constants.constants import VALID_DOMAINS


def is_email_valid(email: str) -> bool:
    """
    This function is being called by the (get_email) one
    It checks if the email is invalid and if it is - the program stops.
    Otherwise, it returns True
    """
    is_valid_email = False

    while True:
        try:
            # If there is not an At symbol - prints out a message
            if '@' not in email:
                raise Exceptions.EmailDoesNotContainsAtSymbolError("Email must contain at least one '@' symbol!")

            # Split the email into 2 parts
            name, domain = email.split('@')

            if '.' not in domain:
                raise Exceptions.DomainMustContainsDot("Domain must contain a dot! '.com'")

            # Check if the length of the first part is shorter or equal to 4 and if it is - throw an exception
            if len(name) <= 4:
                raise Exceptions.NameTooShortError("Name must be more than 4 characters!")

            # Check if the last part of the domain is not in Valid Domains and if it is not - raise an exception
            elif domain.split('.')[1] not in VALID_DOMAINS:
                raise Exceptions.InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net!")

            # Check if there is more than 1 At symbol - stop the program
            elif email.count('@') > 1:
                raise Exceptions.MoreThanOneAtSymbolError("Email must contain only one At symbol!")

            # Check if there is a match with the emails in the database and throw an exception
            elif is_email_used(email):
                raise Exceptions.EmailHasBeenAlreadyUsedError("Email address has been already used by another User!")
        except Exceptions.DomainWithoutDotError as dmcd:
            print(dmcd)
        except Exceptions.NameTooShortError as ntse:
            print(ntse)
        except Exceptions.InvalidDomainError as ide:
            print(ide)
        except Exceptions.MoreThanOneAtSymbolError as mtoa:
            print(mtoa)
        except Exceptions.EmailHasBeenAlreadyUsedError as ehbu:
            print(ehbu)
        except Exceptions.EmailDoesNotContainsAtSymbolError as edca:
            print(edca)
        else:
            is_valid_email = True

        if is_valid_email:
            return True
        return False


def is_password_valid(password) -> str:
    """
    This function check if the password given by the User is valid or not.
    if valid: return: True,
    if not valid: return False,
    """
    # Initialise a boolean in order to know if the password is valid or not

    invalid_pass_messages = []

    # Check the password length
    if not (4 < len(password) < 16):
        invalid_pass_messages.append("Password must have 4 to 16 symbols!")

    # Check the number of digits in it
    number_of_digits = [x for x in password if x.isdigit()]
    if len(number_of_digits) < 2:
        invalid_pass_messages.append("Password must have at least 2 digits!")

    # Check if there is a capital letter in the password
    capital_letters = [x for x in password if x.isupper()]
    if len(capital_letters) < 1:
        invalid_pass_messages.append("Password must have at least 1 capital letter!")

    # Check if there is a special symbol in the password
    for symbol in list(string.punctuation):
        if symbol in list(password):
            break
    else:
        invalid_pass_messages.append("Password must contain at least one special character!")

    return '\n'.join(invalid_pass_messages)  # boolean


def is_email_used(email):
    # Connect to the database
    conn = sqlite3.connect("userdata2.db")
    cur = conn.cursor()

    # Find if there is a match within the database with username, pass
    cur.execute("SELECT * FROM userdata2 where username = ?", (email,))

    if cur.fetchall():
        return True  # if email is used
    else:
        return False  # if email is not in the database
