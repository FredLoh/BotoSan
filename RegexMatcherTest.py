import unittest
from RegexMatcher import RegexMatcher
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity


class RegexMatcherRollTests(unittest.TestCase):
    def setUp(self):
        self.regex_matcher = RegexMatcher()
        self.mock_to = "+1234567890"

    def testSlashRollPattern(self):
        roll_pattern = TextMessageProtocolEntity("/roll testing", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(roll_pattern), True)

    def testNoRollPattern(self):
        false_pattern = TextMessageProtocolEntity("missing the word", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(false_pattern), False)

    def testRollInMiddleOfSentence(self):
        roll_in_middle = TextMessageProtocolEntity("This is a roll test", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(roll_in_middle), True)

    def testMultipleRollsInSentence(self):
        multiple_rolls = TextMessageProtocolEntity("this roll are multiple roll in a sentence", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(multiple_rolls), True)


class RegexMatcherRazaTests(unittest.TestCase):
    def setUp(self):
        self.regex_matcher = RegexMatcher()
        self.mock_to = "+1234567890"

    def testRazaInSentence(self):
        raza_pattern = TextMessageProtocolEntity("pura raza", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(raza_pattern), True)

    def testRazaMultipleTimesInSentence(self):
        multi_raza_pattern = TextMessageProtocolEntity("raza pura raza so", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(multi_raza_pattern), True)

class RegexMatcherBebanTests(unittest.TestCase):
    def setUp(self):
        self.regex_matcher = RegexMatcher()
        self.mock_to = "+1234567890"

    def testBebanInSentence(self):
        beban_pattern = TextMessageProtocolEntity("Hola, BotoSan porfavor insulta a Esteban pronto", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(beban_pattern), True)

    def testBebanMultipleTimesInSentence(self):
        multi_beban_pattern = TextMessageProtocolEntity("BotoSan porfavor insulta a Esteban , BotoSan porfavor insulta a Esteban", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(multi_beban_pattern), True)

    def testBebanMultipleTimesInSentence(self):
        no_beban_pattern = TextMessageProtocolEntity("BotoSan insulta a Esteban", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(no_beban_pattern), False)


if __name__ == '__main__':
    unittest.main()
