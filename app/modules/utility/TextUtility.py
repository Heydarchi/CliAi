# This class will helps to make the text more readable
import colorama
from colorama import Fore, Back, Style


class TextUtility:
    @staticmethod
    def print_code_colorized(text):
        "This method will color the code in the text"
        text = TextUtility.add_color_to_code(text, Fore.GREEN)
        print(text + Style.RESET_ALL)

    @staticmethod
    def print_plus(input):
        "This method will color the code in the text"
        if "DESCRIPTION" in input:
            print("\n".join(input["DESCRIPTION"]) + Style.RESET_ALL)
        if "CONTENT" in input:
            print("\n".join(input["CONTENT"]) + Style.RESET_ALL)
        if "SHELL_SCRIPT" in input:
            if "".join(input["SHELL_SCRIPT"]).strip() != "":
                print(
                    "\nScript:\n"
                    + Fore.LIGHTBLUE_EX
                    + "\n".join(input["SHELL_SCRIPT"])
                    + Style.RESET_ALL
                )
        if "LINKS" in input:
            if "".join(input["LINKS"]).strip() != "":
                print(
                    "\nLinks:\n"
                    + Fore.CYAN
                    + "\n".join(input["LINKS"])
                    + Style.RESET_ALL
                )
        if "KEYWORDS" in input:
            if "".join(input["KEYWORDS"]).strip() != "":
                print(
                    "\nKeywords:\n"
                    + Fore.RED
                    + "\n".join(input["KEYWORDS"])
                    + Style.RESET_ALL
                )
        if "CODE" in input:
            if "".join(input["CODE"]).strip() != "":
                print(
                    "\nCode:\n"
                    + Fore.GREEN
                    + "\n".join(input["CODE"])
                    + Style.RESET_ALL
                )

    @staticmethod
    def print_color(text, color):
        "This method will print the text in the color"
        print(color + text + Style.RESET_ALL)

    @staticmethod
    def print_user(text):
        "This method will print the text in the color"
        print("User: " + Fore.BLUE + text + Style.RESET_ALL)

    @staticmethod
    def add_color_to_code(text, color):
        # This function look for three of \` and color the code between them
        index = 0
        while True:
            index = text.find("```", index)
            if index == -1:
                break
            text = text[:index] + color + text[index + 3 :]
            index += 3
            index = text.find("```", index)
            if index == -1:
                break
            text = text[:index] + Style.RESET_ALL + text[index + 3 :]
            index += 3
        return text


if __name__ == "__main__":
    print(TextUtility.add_color_to_code("```code1``` HEHEE ```code2```", Fore.GREEN))
