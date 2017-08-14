# coding=utf-8
import re
import BasicTextProtocols


class RegexMatcher:
    def __init__(self):
        self.rollPattern = "^/roll"

    def doesMatchAPattern(self, message):
        if re.compile(self.rollPattern).match(message.getBody()):
            return True
        else:
            return False

    def matchPatterns(self, message):
        if re.compile(self.rollPattern).match(message.getBody()):
            return BasicTextProtocols.randomRoll(message)
        return None
