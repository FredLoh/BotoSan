# coding=utf-8
import re
import BasicTextProtocols


class RegexMatcher:
    def __init__(self):
        self.rollPattern = r"\brolls?\b|^/rolls?"
        self.razaPattern = r"\braza\b"
		self.bebanPattern = r"\BotoSan porfavor insulta a Esteban\b"

    def message_matches_a_pattern(self, message):
        """
        Checks if the MessageProtocol matches a regex
        :param message: A object of type MessageProtocol
        :return: Boolean
        """
        if re.search(self.rollPattern, message.getBody()):
            return True
        elif re.search(self.razaPattern, message.getBody()):
            return True
		elif re.search(self.bebanPattern, message.getBody()):
            return True
        else:
            return False

    def generate_message_protocol_for_pattern(self, message):
        """
        Given a message, attempts to match it with a pattern, and return a hydrated message protocol
        containing the appropriate response
        :param message: An object of class MessageProtocol
        :return: A MessageProtocol or None if there is no valid match
        """
        if re.search(self.rollPattern, message.getBody()):
            return BasicTextProtocols.random_roll(message)
        elif re.search(self.razaPattern, message.getBody()):
            return BasicTextProtocols.random_raza(message)
		elif re.search(self.bebanPattern, message.getBody()):
            return BasicTextProtocols.random_esteban(message)
        return None
