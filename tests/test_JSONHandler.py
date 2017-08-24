import unittest

from JSONHandler import JSONHandler


class TestJSONHandler(unittest.TestCase):
    def test_read_in_response_file(self):
        self.assertIsNotNone(JSONHandler.read_in_response_file())

    def test_get_response_for(self):
        self.assertIsNone(JSONHandler.get_response_for("not_a_real_key"))
        self.assertIsNotNone(JSONHandler.get_response_for("adj_list"))
        self.assertGreater(len(JSONHandler.get_response_for("adj_list")), 3)
