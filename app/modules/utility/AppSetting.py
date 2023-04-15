import os
from PythonUtilityClasses.FileWriter import FileWriter
from PythonUtilityClasses.FileReader import FileReader
import os

OUT_DIR = "./out/"
API_KEY_FILE = "openapi_key.txt"
GOOGLE_API_KEY_FILE = "openapi_key.txt"


class AppSetting:
    def __init__(self):
        self.openapi_key = None
        self.googleapi_key = None
        self.config_dir = None

    def init(self):
        self.config_dir = os.environ["CLI_AI_DIR"] + "/config/"
        self._initDirs()
        self._init_openapi_key()

    """If the API key file is not found, get it through the console"""

    def _init_openapi_key(self):
        if not os.path.exists(self.config_dir + API_KEY_FILE):
            self.openapi_key = input("Please enter your OpenAI API key: ")
            FileWriter.write_file(self.config_dir + API_KEY_FILE, self.openapi_key)
        else:
            self.openapi_key = FileReader.read_file(self.config_dir + API_KEY_FILE)

    def _init_googleapi_key(self):
        if not os.path.exists(self.config_dir + GOOGLE_API_KEY_FILE):
            self.googleapi_key = input("Please enter your Google API key: ")
            FileWriter.write_file(self.config_dir + GOOGLE_API_KEY_FILE, self.googleapi_key)
        else:
            self.googleapi_key = FileReader.read_file(self.config_dir + GOOGLE_API_KEY_FILE)

    def _initDirs(self):
        if not os.path.exists(OUT_DIR):
            os.makedirs(OUT_DIR)

        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)

    def get_api_key(self):
        if self.openapi_key == None:
            if self.openapi_key == None:
                raise ValueError("API key is not set")
        return self.openapi_key
