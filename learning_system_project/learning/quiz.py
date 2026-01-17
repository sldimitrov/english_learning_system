import random

from LearningSystem.learning_system_project.constants.messages import menu_options
from LearningSystem.learning_system_project.constants.options import positive_options, negative_options


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
