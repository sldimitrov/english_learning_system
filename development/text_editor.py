from development.translator import Definer


class WriteSentences:
    """ This class is responsible for writing new sentences into the sentences text file """
    @staticmethod
    def write_sentence(sentence: str) -> None:
        """ This method receives a sentence and writes it into the sentences text file """
        with open("D:\\repos\\english\\development\\text_files\\sentences_list.txt", "a") as file:
            file.write(f"{sentence}\n")


class SaveWordsToDictionary:
    """ This class is responsible formatting the word into dictionary format and saving them """
    @staticmethod
    def format(word, definition) -> str:
        """ This method receives (word, definition) and formats them into dictionary format """
        return f"|{word}| - |{definition}|\n"

    @staticmethod
    def save_word_to_dictionary(line) -> None:
        """ This method receives line and writes it into dictionary """
        with open("D:\\repos\\english\\development\\text_files\\dictionary.txt", "a") as dictionary:
            dictionary.write(line)


class NewWords(Definer, SaveWordsToDictionary):
    """ This class is responsible for reading the new words, also for getting their definitions """
    @staticmethod
    def read_file() -> str:
        """ This method read all new words from a text file and return them """
        with open("D:\\repos\\english\\development\\list_of_words.txt", "r") as file:
            data = file.read()
            return data

    def get_words_definition(self) -> list[str] or str:
        """ This method get all new words definition and return them"""
        # Read the new words
        file_data = self.read_file()

        # Initialise a list
        lines = []

        if not file_data:  # check if there are new words
            return 'There are not any new words.'  # TODO: ADD A OPERATION - ADDING NEW WORDS WHEN THE LIST IS EMPTY

        for word in file_data.split('\n'):
            # Extract definition
            definition = self.get_definition(word)

            # Format in dictionary style
            line = self.format(word, definition)

            # Save the line in dictionary
            self.save_word_to_dictionary(line)

            # Append each line to the list
            lines.append(line)

        return lines


class NewWordsDefiner(NewWords):
    """ This is the main class from the highest level.
         It is responsible for getting the new words
       definitions and saving them into the dictionary"""

    @staticmethod
    def save_words(data) -> None:
        """ This method writes the formatted data into a file """
        with open("D:\\repos\\english\\development\\words_with_definitions", "a") as file:
            file.write(''.join(data))

    def define_new_words(self) -> None:
        """ This method match the new words with their definitions and save them """
        words_definitions = self.get_words_definition()
        self.save_words(words_definitions)


# Initialise an instance of the class
definer = NewWordsDefiner()

# Access a method to define all new words
definer.define_new_words()
