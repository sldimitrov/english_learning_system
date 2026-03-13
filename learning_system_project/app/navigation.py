# Navigation
import string

from LearningSystem.learning_system_project.__main__ import access_dictionary, test_knowledge
from LearningSystem.learning_system_project.constants.messages import menu_options, origin_story, ending_message
from LearningSystem.learning_system_project.messaging.prompts import get_input
from PythonAutomation.EnglishWordsScript.Development.__main__ import show_new_words, write_sentences, TextToSpeech

def access_learning():
    """
    The main function contains the functionalities of the entire program and
    calls other functions based on the user's choice.
    """

    # Print the menu to the User and ask for input
    print(menu_options)
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
            print(origin_story)

        elif choice == 7:
            print(ending_message)
            raise SystemExit

        choice = get_input()
