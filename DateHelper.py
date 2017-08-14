from datetime import datetime


class DateHelper:
    def __init__(self):
        pass

    @staticmethod
    def determineIfBotosanShouldRespond(timestamp):
        """
        Determines if botosan should respond given the messages timestamp. Messages older than the threshold
        are ignored,
        :param timestamp: Unix timestamp
        :return: Boolean
        """
        difference = datetime.now() - datetime.fromtimestamp(timestamp)
        return difference.seconds <= 10
