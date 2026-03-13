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
