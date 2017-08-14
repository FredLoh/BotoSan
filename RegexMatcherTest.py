import unittest
from RegexMatcher import RegexMatcher


class RegexMatcherTests(unittest.TestCase):
    def testRollPattern(self):
        regexMatcher = RegexMatcher()
        rollPattern = "/roll testing"
        falsePattern = "missing the word"
        rollInMiddle = "This is a roll test"

        self.assertEqual(regexMatcher.doesMatchAPattern(rollPattern), True)
        self.assertEqual(regexMatcher.doesMatchAPattern(falsePattern), False)
        self.assertEqual(regexMatcher.doesMatchAPattern(rollInMiddle), True)

if __name__ == '__main__':
    unittest.main()