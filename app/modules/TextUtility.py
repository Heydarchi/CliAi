#This class will helps to make the text more readable
import colorama
from colorama import Fore, Back, Style

class TextUtility:
    @staticmethod
    def print_code_colorized(text):
        'This method will color the code in the text'
        return text

    @staticmethod
    def print_color(text, color):
        'This method will print the text in the color'
        print(color + text + Style.RESET_ALL)
