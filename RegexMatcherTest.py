import unittest

from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

from RegexMatcher import RegexMatcher


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
        raza_pattern = TextMessageProtocolEntity("pura /raza", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(raza_pattern), True)

    def testRazaMultipleTimesInSentence(self):
        multi_raza_pattern = TextMessageProtocolEntity("/raza pura /raza so", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(multi_raza_pattern), True)


class RegexMatcherBebanTests(unittest.TestCase):
    def setUp(self):
        self.regex_matcher = RegexMatcher()
        self.mock_to = "+1234567890"

    def testBebanInSentence(self):
        beban_pattern = TextMessageProtocolEntity("Hola, BotoSan porfavor insulta a Esteban pronto", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(beban_pattern), True)

    def testBebanMultipleTimesInSentence(self):
        multi_beban_pattern = TextMessageProtocolEntity(
            "BotoSan porfavor insulta a Esteban , BotoSan porfavor insulta a Esteban", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(multi_beban_pattern), True)

    def testBebanDoesNotShowInSentence(self):
        no_beban_pattern = TextMessageProtocolEntity("BotoSan insulta a Esteban", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(no_beban_pattern), False)


class RegexMatchEightballTests(unittest.TestCase):
    def setUp(self):
        self.regex_matcher = RegexMatcher()
        self.mock_to = "+1234567890"

    def testSlashRollPattern(self):
        o_gran_pattern = TextMessageProtocolEntity("o gran botosan cual es el", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(o_gran_pattern), True)

    def testNoRollPattern(self):
        false_pattern = TextMessageProtocolEntity("no aparece el sentence", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(false_pattern), False)

    def testRollInMiddleOfSentence(self):
        oh_grande_botosan = TextMessageProtocolEntity("oh grande botosan tesing", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(oh_grande_botosan), True)

    def testUppercaseOhGran(self):
        oh_grande_botosan = TextMessageProtocolEntity("Oh GRAN BoToSAN tesing", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(oh_grande_botosan), True)

    def testgrandioso(self):
        false_pattern = TextMessageProtocolEntity("Testing oh grandioso botosan testing ", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(false_pattern), True)

    def testMisericordiosoTestSinRey(self):
        oh_grande_botosan = TextMessageProtocolEntity("oh misericordioso botosan tesing", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(oh_grande_botosan), True)

    def testMisericordiosoTestConRey(self):
        oh_grande_botosan = TextMessageProtocolEntity("Oh misericordioso rey BoToSAN tesing", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(oh_grande_botosan), True)

    def testAll(self):
        oh_grande_botosan = TextMessageProtocolEntity("Oh grandioso misericordioso rey BoToSAN tesin", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(oh_grande_botosan), True)

    def testSimple(self):
        oh_grande_botosan = TextMessageProtocolEntity("Oh botosan es el mejor", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(oh_grande_botosan), True)


class RegexMatcherJorgeTests(unittest.TestCase):
    def setUp(self):
        self.regex_matcher = RegexMatcher()
        self.mock_to = "+1234567890"

    def testBebanInSentence(self):
        jorge_pattern = TextMessageProtocolEntity("Hola, BotoSan jorgita cacashita test", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(jorge_pattern), True)

    def testBebanMultipleTimesInSentence(self):
        jorgita_cacashita_single = TextMessageProtocolEntity(
            "jorgita cacashita", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(jorgita_cacashita_single), True)

    def testBebanDoesNotShowInSentence(self):
        jorgita_no_cacashita = TextMessageProtocolEntity("jorgita no cacashita", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(jorgita_no_cacashita), False)


class RegexMatcherPatoTests(unittest.TestCase):
    def setUp(self):
        self.regex_matcher = RegexMatcher()
        self.mock_to = "+1234567890"

    def testBebanInSentence(self):
        pato_pattern = TextMessageProtocolEntity("Hola, BotoSan patito pollito test", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(pato_pattern), True)

    def testBebanMultipleTimesInSentence(self):
        patito_pollito_single = TextMessageProtocolEntity(
            "patito pollito", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(patito_pollito_single), True)

    def testBebanDoesNotShowInSentence(self):
        patito_no_pollito = TextMessageProtocolEntity("patito no pollito", to=self.mock_to)
        self.assertEqual(self.regex_matcher.message_matches_a_pattern(patito_no_pollito), False)


if __name__ == '__main__':
    unittest.main()
