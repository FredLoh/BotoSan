import unittest
import env
import time

from DateHelper import DateHelper


class TestDateHelper(unittest.TestCase):
    def test___init__(self):
        assert True

    def test_determine_if_botosan_should_respond(self):
        timestamp = time.time()
        self.assertEqual(True, DateHelper.determine_if_botosan_should_respond(timestamp=timestamp))


if __name__ == '__main__':
    unittest.main()
