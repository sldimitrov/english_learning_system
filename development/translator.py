import requests


class ApiRequest:
    """ This class is responsible for handling requests from the API server. """
    @staticmethod
    def get_response(word):
        """ This method requests the API server with GET and returns the response """
        return requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    @staticmethod
    def get_json(some_text: str):
        """ This method call the get_response method and return its response in JSON format """
        response = ApiRequest.get_response(some_text)

        return response.json()


class Definer:
    """ This class is mainly responsible for getting words definitions """

    @staticmethod
    def get_definition(some_text: str) -> str:
        """ This method get the words definitions.
        receives: word: str
        Call get_response method and use its response to extract the word definition.
        returns: str """
        response = ApiRequest.get_response(some_text)

        try:
            definition = response.json()[0]['meanings'][1]['definitions'][0]['definition']
        except (IndexError, ValueError, KeyError):
            return "Unknown word"

        return definition


