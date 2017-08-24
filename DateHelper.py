from datetime import datetime


class DateHelper:
    def __init__(self):
        pass

    @staticmethod
    def determine_if_botosan_should_respond(timestamp):
        """
        Determines if botosan should respond given the messages timestamp. Messages older than the threshold
        are ignored,
        :param timestamp: Unix timestamp
        :return: Boolean
        """
        difference = datetime.now() - datetime.fromtimestamp(timestamp)
        return abs(difference.seconds) <= 10
