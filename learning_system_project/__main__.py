import sqlite3
import hashlib
import string
import random
import constants
import TextToSpeech
import Exceptions
import textOperations

# TODO: This program does not use python's modularity,
# everything could be split into pieces for easier maintaince
# Each class and method is well documented!

# TODO: There should be a dictionary containing all labels,
# This will help with adding language support in the future.

# TODO: Tests should be added, "System that does not contain tests is broken by design".

# Define plenty of functions
def reg_or_log_user():
    # TODO: Use some constants for the answers would make sense, as we use them much
    while True:
        answer = input("\nDo you have an existing account? (y/n): ").lower()
        if answer == "y" or answer == "yes":
            if login_user():
                return True
            else:
                break

        # TODO: outsource and use
        # negative_choices = ["n", "no"]
        # if negative_choices.contains(answer):

        elif answer == "n" or answer == "no":
            # TODO: Add a function for the input and just pass the label
            choice = input("Would you like to create a new account? (y/n): ").lower()

            if choice == "y" or choice == "yes":
                if register_user():
                    print(f'-You were successfully registered!\n')
                    if login_user():
                        return True

                    else:
                        break

            elif choice == "n" or choice == "no":
                print("\nProgram ends here...")
                raise SystemExit

        # This logic is hard to hear
        else:
            if answer:
                print("Unknown answer: " + answer)
            else:
                print("Please input a valid answer")
            continue

    return False


def get_email():
    """
    This function is being called by the main in order to get
    the email address of the user.
    It also calls the 1-(print_messages) and the 2-(is_email_valid) functions
    The first one prints out the email validation rules.
    If the second one returns true, the function returns the email to the main.
    """

    while True:
        textOperations.print_messages(get_email.__name__)
        user_email = input("Enter an email address, please: ")
        is_valid_email = is_email_valid(user_email)
        if is_valid_email:
            return user_email


# TODO: Outsource in validation file
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
            elif domain.split('.')[1] not in constants.VALID_DOMAINS:
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
        textOperations.print_messages(get_password.__name__)

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


# Good use of python annotations
def write_sentences() -> bool:
    """
    The function `write_sentences` reads words and their definitions from a text file,
    prompts the user to enter sentences related to each word, saves the sentences into
    a separate text file, and saves the words and their definitions into a dictionary.
    :return: a boolean value `True`.
    """
    lines = []

    # Read the data from the text file and append it into a list
    data = open('text_files/list_of_words.txt', 'r')
    for d in data:
        if '\n' in d:
            d = d.replace('\n', '')
        if d:
            lines.append(d)

    words_dictionary = {}
    sentences = []

    if lines:
        for line in lines:
            if line:  # if it's not a blank line
                # Split the line by ("-") in order to get the word and its definition
                word, definition = line.split('-')
                print(f'\nWord or a phrase found: {word}')
                print(f'Definition: {definition}')

                # Collect sentences into a list
                sentence = input('Show imagination: ')
                sentences.append(sentence)
                print('Sentence saved successfully')

                # Save the word with its definition into a dictionary
                words_dictionary[word] = definition

                # Remove the written words from the (words text file)
                f = open('text_files/list_of_words.txt', 'r')
                text = f.read()
                text = text.replace(line, '')
                f.close()
                f = open('text_files/list_of_words.txt', 'w')
                f.write(text)
                f.close()
                print()
    else:
        print('There are not any new words in order to write sentences with them.')

    # Very clear separation of logic blocs
    # Save the sentences into a text file
    file = open('text_files/sentences_list.txt', 'a')
    file.write('\n')
    file.write('\n'.join(sentences))
    file.close()

    # Save the words and their definitions into the dictionary
    file = open('text_files/dictionary.txt', 'a')
    for key, value in words_dictionary.items():
        file.write(f'{key} - {value}\n')
    file.close()
    return True


def access_dictionary() -> bool:
    """
    The function `access_dictionary` reads a file called "dictionary.txt" and checks if it contains any words, returning
    True if it does and printing the line if they are alphabetical.
    :return: a boolean value.
    """
    f = open('text_files/dictionary.txt', 'r')
    data = f.read()
    if data:
        print("\nAll the words that are in the dictionary:")
        for line in data:
            if line.isalpha():
                print(data)
                f.close()
                return True
    else:
        print('\nThere are not any words in the dictionary.')
        return True


def show_new_words() -> bool:
    """
    The function `show_new_words` reads a file called "list_of_words.txt" and prints all the alphabetic characters in
    the file, indicating that they are new words. If there are no new words, it prints a message indicating that the
    list is empty.
    :return: a boolean value.
    """
    f = open('list_of_words.txt', 'r')
    data = f.read()
    for _ in data:
        if _.isalpha():
            print('\nList of all new words:')
            print(data)
            f.close()
            return True
    else:
        print('There are not any new words.')   # ADD A OPERATION - ADDING NEW WORDS WHEN THE LIST IS EMPTY
        return True


# Build a game with text transform skills, awesome!
def test_knowledge():
    """
    The function `test_knowledge()` allows the user to play a game where they are given a word, and they have to provide
    its definition.
    :return: The function `test_knowledge` returns a boolean value `True`.
    """
    data = open('text_files/dictionary.txt', 'r')   # Open the text file
    lines = []
    # Remove all the new lines from the data in order to save each line in a list
    # Save the data into a list
    for d in data:
        if '\n' in d:
            d = d.replace('\n', '')
        if d:
            lines.append(d)
    if lines:
        # Let the User choose a game type
        print('Here you will be able to check your knowledge.\n'
              'Please choose a game-type\n'
              '(s) for a short one\n'
              'and (l) for a longer one'
              '...')
        answer = input()
        if answer == 's':
            n = 10
        elif answer == 'l':
            n = 20
        else:
            print('Error: Invalid Input')
            return True

        # Choose a random word from the list and ask the user for its definition
        points = 0
        bad_words = []
        for _ in range(n):
            number = random.randint(0, len(lines) - 1)
            line = lines[number]
            word, definition = line.split('-')
            print(f'\nThe given words is: {word}')
            _back = input('What is the definition?: ')

            print(f'\nThe definition is: {definition}')
            signal = input('Did you answer correctly? (y/n): ')
            if signal.lower() == 'y':
                points += 1
                print('+1 point')
            elif signal.lower() == 'n':
                bad_words.append(line)

        # TODO: Introduce a mapper here
        if answer == 's':
            if points <= 3:
                print('\nYou still have much to learn, buddy!\n'
                      f'Points: {points}:10')
            elif 3 < points <= 5:
                print('\nYou are in the middle gold, motivate yourself to do better!\n'
                      f'Points: {points}/10')
            elif 5 < points <= 8:
                print('\nGood job! Keep learning!\n'
                      f'Points: {points}/10')
            elif 8 < points <= 10:
                print('\nExcellent!\n'
                      f'Points: {points}/10')

        # Replace with a mapper
        elif answer == 'l':
            if points <= 6:
                print('\nYou still have much to learn, buddy!\n'    
                      f'Points: {points}/20')
            elif 6 < points <= 10:
                print('\nYou are in the middle gold, motivate yourself to do better!\n' 
                      f'Points: {points}/20')
            elif 10 < points <= 16:
                print('\nGood job! Keep learning!\n'
                      f'Points: {points}/20')
            elif 16 < points <= 20:
                print('\n'
                      'Excellent! -------\n'              
                      f'Points: {points}/20\n'
                      f'------------------')
        else:
            print('Wrong game-type inputted')
            return True
        return True

    else:   # No words in the dictionary:
        print('There are not any words in your dictionary.')
        textOperations.menu()

# This and the other 2 functions below are responsible for the input
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



# Define a function
def input_validator(message: str):
    """
    This functions checks if the choice of the user occurs in the valid list of answers
    If not: the (handle invalid input) func. is being called.
    :param message: string
    :return: str / bool
    """

    if message not in constants.valid_answers:
        message = handle_invalid_input(message)
        return message
    return True


# Define a function
def handle_invalid_input(some_input: str):
    """
    Returns an error message every time it is called
    :param some_input: string
    :return: str
    """
    return f'Error: {some_input} is an invalid input\n'


# Handling such cases makes all the difference
def authentication_failure():
    print("Authentication failed!")
    raise SystemExit


def access_learning():
    """
    The main function contains the functionalities of the entire program and
    calls other functions based on the user's choice.
    """

    # Print the menu to the User and ask for input
    print(textOperations.menu())
    choice = get_input()
    while True:
        if choice.lower() == 'm':
            access_learning()

        if choice not in string.digits:
            print(f"Please, enter a valid choice!\n")
            access_learning()

        choice = int(choice)

        # TODO: Replace with a mapper
        if choice == 1:
            show_new_words()

        elif choice == 2:
            write_sentences()

        elif choice == 3:
            access_dictionary()

        elif choice == 4:
            test_knowledge()

        elif choice == 5:
            TextToSpeech.text_to_speech()

        elif choice == 6:
            print(textOperations.show_info())

        elif choice == 7:
            textOperations.end_the_program()

        choice = get_input()


def main():
    """
    TODO: (4)

    Configuration:
        (1) re-write the whole program using classes
    Learning System:
        (1) record your own voice reading the sentences
        (2) add a dictionary API for the translations
        (3) test_word_knowledge - 1 minute (quick-game)
    Authentication:
        (1) add more extensions for the email
    """
    textOperations.greet_user()

    # Register and or login the user
    if reg_or_log_user():
        print("\nSoftware accessed...")
        access_learning()
    else:
        authentication_failure()


if __name__ == '__main__':
    main()
