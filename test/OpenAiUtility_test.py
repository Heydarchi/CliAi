#This is a test file for the OpenAiUtility class
import unittest
from scripts.OpenAiUtility import OpenAiUtility

class MyTestCase(unittest.TestCase):
    def test_init(self):
        open_ai_util = OpenAiUtility()
        self.assertEqual(open_ai_util.is_api_key_set, False)

    def test_init_open_ai(self):
        open_ai_util = OpenAiUtility()
        open_ai_util.init_open_ai("test")
        self.assertEqual(open_ai_util.is_api_key_set, True)

