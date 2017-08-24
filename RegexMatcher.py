# coding=utf-8
import re

import BasicTextProtocols


class RegexMatcher:
    def __init__(self):
        self.rollPattern = r"\brolls?\b|^/rolls?"
        self.razaPattern = r" ?/raza\b"
        self.bebanPattern = r"\bBotoSan porfavor insulta a Esteban\b"
        self.oGranPattern = r"\boh?\s?(?:gran(de|dioso)?)?\s?(?:misericordioso\s?)?(?:rey\s?)?botosan\b"
        self.jorgitoPattern = r"\bjorgita cacashita\b"
        self.patoPattern = r"\bpatito pollito\b"
        self.triggerPatterns = [self.rollPattern, self.razaPattern, self.bebanPattern, self.oGranPattern,
                                self.jorgitoPattern, self.patoPattern]

    def message_matches_a_pattern(self, message):
        """
        Checks if the MessageProtocol matches a regex
        :param message: A object of type MessageProtocol
        :return: Boolean
        """
        for pattern in self.triggerPatterns:
            if re.compile(pattern, re.IGNORECASE).search(message.getBody()):
                return True
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
            return BasicTextProtocols.random_estaban(message)
        elif re.compile(self.oGranPattern, re.IGNORECASE).search(message.getBody()):
            return BasicTextProtocols.generate_eightball(message)
        elif re.compile(self.jorgitoPattern, re.IGNORECASE).search(message.getBody()):
            return BasicTextProtocols.generate_jorgita_message(message)
        elif re.compile(self.patoPattern, re.IGNORECASE).search(message.getBody()):
            return BasicTextProtocols.generate_pato_message(message)
        return None
