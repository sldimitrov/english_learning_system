import requests


class ApiRequest:
    @staticmethod
    def get_response(word):
        return requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")


class Translator:

    @staticmethod
    def get_json(some_text: str):
        response = ApiRequest.get_response(some_text)

        return response.json()

    @staticmethod
    def get_definition(some_text: str):
        response = ApiRequest.get_response(some_text)

        try:
            definition = response.json()[0]['meanings'][1]['definitions'][0]['definition']
        except (IndexError, ValueError, KeyError):
            return "Unknown word"

        return definition


class TranslatorApp(Translator, ApiRequest):
    @staticmethod
    def define_word(word: str):
        definition = Translator.get_definition(word)
        return f"Definition: {definition}"


# Initialise an object that can be used to translate words
definer = TranslatorApp

print(definer.get_json("hello"))

# Print the definition of a word using the (define_word) method
# print(definer.define_word("splash"))


