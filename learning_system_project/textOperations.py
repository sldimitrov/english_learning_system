import constants
import time

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

def show_info():
    """
    The function "show_info" returns a message that provides an overview of the program and its purpose.
    :return: string (info)
    """
    # TODO: Outsource message
    message = """
               The idea about this program came up into my mind at the end of 2023. I used my own hands and everything
              I have learned since my programming journey had started to make my dream come true. The mission is to help
              others as they develop their skills of learning. In SoftUni they do exactly that - they teach you how to
              study. My program will help each one of you to rememberer new words and conquer a world full of wonders!
                   How to use it?
                First of all, you want to save all of your new words in the <list_of_words.txt>,every one on a single
              line with dash and its definition - (apple - red fruit) and so on...
                After the first step is done you will re-run the program and you can start writing sentences with (2)
              from the menu options.   In no time you'll have learned many new words and each one of them is going to be
              stored in your imaginary dictionary (3)   Within the forth operation (4) you are not only going to learn. 
              You're going to be challenged! Choose it and go and face your demons or stay the same forever!
                Last but not least, the (5) is the latest function of the program in which you can hear all of your 
              sentences read by the computer with human voice. Yeah, I know it sound strange but today everything 
              is possible!   If information is all you have needed at this point choose (7) to exit the temple.
              I will be waiting for your return, because I hope that your learning will be an endless process!
              """
    return message


# Very good idea of using long messages and having a menu
def menu() -> str:
    """
    The `menu` function returns a string containing a user menu with several options.
    :return: a string that contains the user menu options.
    """
    # TODO: Outsource
    menu_message = ('Please, choose an operation (1/2/3/4/5/6/7):\n'
                    '1. See the new words\n'
                    '2. Write down some sentences\n'
                    '3. Open the dictionary\n'
                    '4. Test your knowledge\n'
                    '5. Listen to the written sentences\n'
                    '6. Info\n'
                    '7. Exit the program')
    return menu_message


def print_messages(func_name: str) -> None:
    """
    This function is being called from many others.
    Its purpose is to different print messages to the User,
    depending on the function which have called it.
    """
    message = ""

    # TODO: Outsource func_name and messages

    # Print a message about Valid Email Requirements
    if func_name == "get_email":
        message = (
            f"""
    {'<->-<->' * 6}
        Valid email requirements!\n
        (1) It must consist only 1 At symbol '@'!
        (2) The length of its first part should
        be more than 4 characters!
        (3) The domain must be one of the following: 
            {', '.join(constants.VALID_DOMAINS)}!
                   !!!Warning!!!
         THERE ARE 3 REQUIREMENTS ABOUT THE PASSWORD
    {'<->-<->' * 6}
            """
        )

    elif func_name == "get_password":
        message = (
            f"""
        {'<->-<->' * 6}
            Rules about valid password!\n
            (1) Must be between 4 and 16 symbols!
            (2) At least two digits ought to be used!
            (3) One special character have to be used!
            (4) One capital letter as well!
        {'<->-<->' * 6}
            """
        )

    print(message)


def end_the_program():
    # Greetings for an end
    # TODO: Outsource
    print('\n  Thank yourself for the time you spent learning!\n'
          'I am so happy that you have just used my program!\n'
          'If you had seen any bugs or if you have any ideas\n'
          'how I should improve my learning system, send me\n'
          'an email me here:\n'
          ' -slavidimitrov54@gmail.com\n'
          '                    Best wishes,\n'
          '                    SD')
    raise SystemExit
