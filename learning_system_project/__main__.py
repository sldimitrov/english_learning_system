import random

from LearningSystem.learning_system_project.app.auth_flow import reg_or_log_user
from LearningSystem.learning_system_project.app.navigation import access_learning
from LearningSystem.learning_system_project.messaging.printer import authentication_failure, greet_user
from constants.messages import menu_options
from constants.options import positive_options, negative_options

# TODO: This program does not use python's modularity,
# everything could be split into pieces for easier maintaince
# Each class and method is well documented!

# TODO: There should be a dictionary containing all labels,
# This will help with adding language support in the future.

# TODO: Tests should be added, "System that does not contain tests is broken by design".

# Learning
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

# Learning
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

# Learning
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

# Learning
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
            if signal.lower() in positive_options:
                points += 1
                print('+1 point')
            elif signal.lower() in negative_options:
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
        print(menu_options)

# Navigation
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
    greet_user()

    # Register and or login the user
    if reg_or_log_user():
        print("\nSoftware accessed...")
        access_learning()
    else:
        authentication_failure()

if __name__ == '__main__':
    main()
