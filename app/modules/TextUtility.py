#This class will helps to make the text more readable
import colorama
from colorama import Fore, Back, Style

class TextUtility:
    @staticmethod
    def print_code_colorized(text):
        'This method will color the code in the text'
        text = TextUtility.add_color_to_code(text, Fore.GREEN)
        print(text)

    @staticmethod
    def print_color(text, color):
        'This method will print the text in the color'
        print(color + text + Style.RESET_ALL)

    @staticmethod
    def add_color_to_code(text, color):
        #This function look for thre of \` and color the code between them
        index = 0
        while True:
            index = text.find("```", index)
            if index == -1:
                break
            text = text[:index] + color + text[index+3:]
            index += 3
            index = text.find("```", index )
            if index == -1:
                break
            text = text[:index] + Style.RESET_ALL + text[index+3:]
            index += 3
        return text


if __name__ == "__main__":
    print(TextUtility.add_color_to_code("```code1``` HEHEE ```code2```", Fore.GREEN))
