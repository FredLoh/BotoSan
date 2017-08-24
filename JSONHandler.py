import json


class JSONHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_in_response_file():
        try:
            with open('boto-responses.json') as data_file:
                return json.load(data_file)
        except EnvironmentError:
            return None

    @staticmethod
    def get_response_for(response_key):
        try:
            return JSONHandler.read_in_response_file()[response_key]
        except KeyError:
            return None
