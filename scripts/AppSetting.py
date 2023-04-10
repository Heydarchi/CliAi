import os
from scripts.PythonUtilityClasses.FileWriter import FileWriter

OUT_DIR = "out/"
CONFIG_DIR = "config/"
API_KET_FILE = "api_key.txt"


class AppSetting:
    def __init__(self):
        self.api_key = None

    def init(self):
        self._initDirs()
        self._init_api_key()

    """If the API key file is not found, get it through the console"""

    def _init_api_key(self):
        if not os.path.exists(CONFIG_DIR + API_KET_FILE):
            self.api_key = input("Please enter your OpenAI API key: ")
            FileWriter.write_file(CONFIG_DIR + API_KET_FILE, self.api_key)

    def _initDirs(self):
        if not os.path.exists(OUT_DIR):
            os.makedirs(OUT_DIR)

        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)

    def get_api_key(self):
        if self.api_key == None:
            if self.api_key == None:
                raise ValueError("API key is not set")
        return self.api_key
