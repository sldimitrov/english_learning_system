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
