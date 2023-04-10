from modules.OpenAiUtility import OpenAiUtility
from modules.AppSetting import AppSetting
from PythonUtilityClasses.FileReader import FileReader
from modules.TextUtility import TextUtility
import argparse

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
            description="CliAi Makes it possible to chat with ChatGPT through the command line.")
        parser.add_argument("mode", help="Run in the char mode. Put the message or the file name after the one-shoe/file", type=str,
                            choices=["chat", "one-shot","file"], default="one-shot")
        parser.add_argument("args", nargs='+', help="Additional arguments")
        args = parser.parse_args()
        return args

    def run(self):
        args = self.init_help()
        if args.mode == "chat":
            self.run_chat()
        elif args.mode == "one-shot":
            self.run_one_shot(args.args[0])
        elif args.mode == "file":
            self.run_file(args.args[0])
        else:
            print("Invalid mode")

    def run_chat(self):
        while True:
            user_input = input("You: ")
            if user_input == "exit":
                break
            print("Please wait for the response...")
            TextUtility.print_code_colorized(self.open_ai_util.chat(user_input))
    def run_one_shot(self, message):
        print("Please wait for the response...")
        TextUtility.print_code_colorized(self.open_ai_util.chat(message))

    def run_file(self, file_name):
        print("Please wait for the response...")
        file_content = FileReader.read_file(file_name)
        response = self.open_ai_util.chat(file_content)
        TextUtility.print_code_colorized(response)



if __name__ == "__main__":
    """Here we handle user input and output and process the input arguments
    to run the right function."""
    app = App()
    app.run()

