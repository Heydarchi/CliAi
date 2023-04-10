import os
from PythonUtilityClasses.FileWriter import FileWriter
from PythonUtilityClasses.FileReader import FileReader
import os

OUT_DIR = "./out/"
API_KET_FILE = "api_key.txt"


class AppSetting:
    def __init__(self):
        self.api_key = None
        self.config_dir = os.environ["CLI_AI_DIR"] + "/config/"

    def init(self):
        self._initDirs()
        self._init_api_key()

    """If the API key file is not found, get it through the console"""

    def _init_api_key(self):
        if not os.path.exists(self.config_dir + API_KET_FILE):
            self.api_key = input("Please enter your OpenAI API key: ")
            FileWriter.write_file(self.config_dir + API_KET_FILE, self.api_key)
        else:
            self.api_key = FileReader.read_file(self.config_dir + API_KET_FILE)

    def _initDirs(self):
        if not os.path.exists(OUT_DIR):
            os.makedirs(OUT_DIR)

        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)

    def get_api_key(self):
        if self.api_key == None:
            if self.api_key == None:
                raise ValueError("API key is not set")
        return self.api_key
