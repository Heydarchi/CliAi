import unittest
from modules.TextUtility import TextUtility
from colorama import Fore, Back, Style


class MyTestCase(unittest.TestCase):
    def test_add_color_to_code(self):
        text = "```code```"
        text = TextUtility.add_color_to_code(text, Fore.GREEN)
        self.assertEqual(text, Fore.GREEN + "code" + Style.RESET_ALL)

    def test_add_color_to_code_with_multiple_code(self):
        text = "```code1``` ```code2```"
        text = TextUtility.add_color_to_code(text, Fore.GREEN)
        self.assertEqual(text, Fore.GREEN + "code1" + Style.RESET_ALL + " " + Fore.GREEN + "code2" + Style.RESET_ALL)


    def test_add_color_to_code_with_multiple_code_and_text(self):
        text = "```code1``` Text1 ```code2``` Text2"
        text = TextUtility.add_color_to_code(text, Fore.GREEN)
        self.assertEqual(text, Fore.GREEN + "code1" + Style.RESET_ALL + " Text1 " + Fore.GREEN + "code2" + Style.RESET_ALL + " Text2")