
class Write:
    @staticmethod
    def write_sentence(sentence: str):
        with open("D:\\repos\\english\\development\\text_files\\sentences_list.txt", "a") as w:
            w.write(f"{sentence}\n")


class SaveDictionary:
    @staticmethod
    def save_word_to_dictionary(word: str, definition: str):
        with open("D:\\repos\\english\\development\\text_files\\dictionary.txt", "a") as s:
            s.write(f"{word} - {definition}")


class TextEditor(Write, SaveDictionary):
    pass


pen = Write()

# first = '123'
# second = '566'
# pen.write_sentence(second)
