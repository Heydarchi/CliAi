from app.modules.ai.OpenAiUtility import OpenAiUtility
from app.modules.utility.AppSetting import AppSetting
from PythonUtilityClasses.FileReader import FileReader
from app.modules.utility.TextUtility import TextUtility
import argparse
from colorama import Fore, Style

# This file contains the main logic for the app


class App:
    def __init__(self):
        self.app_setting = AppSetting()
        self.open_ai_util = OpenAiUtility()
        self.init_app()

    def init_app(self):
        self.app_setting.init()
        self.open_ai_util.init_open_ai(self.app_setting.get_api_key())

    def init_help(self):
        parser = argparse.ArgumentParser(
            description="CliAi Makes it possible to chat with ChatGPT through the command line."
        )
        parser.add_argument(
            "mode",
            help="Run in the char mode. Put the message or the file name after the one-shoe/file",
            type=str,
            choices=["chat", "oneshot", "file"],
            default="oneshot",
        )
        parser.add_argument("args", nargs="*", help="Additional arguments")
        args = parser.parse_args()
        return args

    def run(self):
        args = self.init_help()
        # TextUtility.print_user(" ".join(args.args), Fore.CYAN )
        if args.mode == "chat":
            self.run_chat()
        elif args.mode == "oneshot":
            msg = args.args[0]
            if len(args.args) > 1:
                msg = " ".join(args.args[0:])
            self.run_one_shot(msg)
        elif args.mode == "file":
            msg = ""
            if len(args.args) > 2:
                msg = " ".join(args.args[2:])
            self.run_file(args.args[1], msg)
        else:
            print("Invalid mode")

    def run_chat(self):
        while True:
            user_input = input(Fore.LIGHTBLUE_EX + "You: ")
            print(Style.RESET_ALL, end="")
            if user_input == "exit" or user_input == "quit":
                break
            TextUtility.print_color("Please wait for the response...", Fore.YELLOW)
            TextUtility.print_code_colorized(self.open_ai_util.chatPlus(user_input))

    def run_one_shot(self, message):
        print("Running in oneshot mode" + "\nMessage:" + str(message))
        TextUtility.print_color("Please wait for the response...", Fore.YELLOW)
        TextUtility.print_code_colorized(self.open_ai_util.chatPlus(message))

    def run_file(self, file_name, msg):
        print(
            "Running in file mode"
            + "\nFile name: "
            + str(file_name)
            + "\nMessage: "
            + str(msg)
        )
        TextUtility.print_color("Please wait for the response...", Fore.YELLOW)
        file_content = FileReader.read_file(file_name)
        response = self.open_ai_util.chatPlus(file_content + "\n" + msg)
        TextUtility.print_code_colorized(response)


if __name__ == "__main__":
    """Here we handle user input and output and process the input arguments
    to run the right function."""
    app = App()
    app.run()
