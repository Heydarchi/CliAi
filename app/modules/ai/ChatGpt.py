from modules.ai.OpenAiUtility import OpenAiUtility
from modules.utility.AppSetting import AppSetting
from json import dumps


class ChatGpt:
    def __init__(self):
        self._app_setting = AppSetting()
        self._app_setting.init()
        self._open_ai_util = OpenAiUtility()
        self._open_ai_util.init_open_ai(self._app_setting.get_api_key())
        self._init_variables()

    def _init_variables(self):
        self._SHELL_SCRIPT = '!!SHELL_SCRIPT!!=["Content_1", "Content2", "Content3"]'
        self._CODE = '!!CODE!!=["the_provided_code"]'
        self._FILE = '!!FILE!!=["the_provided_file"]'
        self._CONTENT = '!!CONTENT!!=["the_provided_content"]'
        self._LINKS = '!!LINKS!!=["Link_1", "Link2", "Link3"]'
        self._KEYWORDS = '!!KEYWORDS!!=["the_provided_keywords"]'
        self._DESCRIPTION = '!!DESCRIPTION!!=["the_provided_description"]'
        self._ASK_FOR_SHELL_SCRIPT = (
            "Please provide the shell script you want to run like\n "
            + self._SHELL_SCRIPT
        )

        self._ASK_FOR_LINKS = (
            " Please only respond with 2 links you want to scrap int the format below \n"
            + self._LINKS
        )
        self._ASK_FOR_KEYWORDS = (
            " Please suggest some keywords to search for the user input above"
            " separated by a comma like \n" + self._KEYWORDS
        )
        self._ASK_FOR_CONTENT = (
            " Please provide the output in format below:\n" + self._CONTENT
        )

        self._ASK_TO_SUMMARIZE = (
            " Please summarize and extract the key information for:\n"
        )

        self._ASK_FOR_OUTPUT_OR_CONTINUE_SEARCH = (
            " If the content provided is enough provide the output"
            " content/code/file/etc for user provide like below: \n"
            + self._SHELL_SCRIPT
            + self._CODE
            + self._FILE
            + self._CONTENT
            + "If the content provided is not enough provide the keywords"
            + self._KEYWORDS
        )

        self._ASK_FOR_OUTPUT = (
            " Please provide the output in format below if any of them "
            "is available other wise ignore the irrelevant tags:\n"
            + self._DESCRIPTION
            + self._SHELL_SCRIPT
            + self._CODE
            + self._CONTENT
        )

    def init(self):
        self._app_setting.init()
        self._open_ai_util.init_open_ai(self._app_setting.get_api_key())

    def chat(self, msg):
        return self._open_ai_util.chatPlus(msg)

    def chatPlus(self, msg):
        return self._open_ai_util.chatPlus(msg + self._ASK_FOR_OUTPUT)

    def ask_for_keywords(self, prompt):
        print("Asking for keywords: ", prompt + self._ASK_FOR_KEYWORDS)
        return self._open_ai_util.chatPlus(self._ASK_FOR_KEYWORDS + prompt)

    def select_links_to_scrap(self, results):
        print("Asking for links to scrap: ", results)
        return self._open_ai_util.chatPlus(self._ASK_FOR_LINKS + dumps(results))

    def process_scrapped_data(self, scrapped_contents):
        print(
            "Asking for processing scrapped data: ",
            scrapped_contents,
        )
        return self._open_ai_util.chatPlus(
            self._ASK_FOR_OUTPUT_OR_CONTINUE_SEARCH + dumps(scrapped_contents)
        )

    def ask_for_content(self, prompt):
        print("Asking for content: ", prompt)
        return self._open_ai_util.chatPlus(
            self._ASK_FOR_OUTPUT_OR_CONTINUE_SEARCH + dumps(prompt)
        )

    def ask_for_shell_script(self, prompt):
        print("Asking for shell script: ", prompt)
        return self._open_ai_util.chatPlus(prompt + self._ASK_FOR_SHELL_SCRIPT)

    def ask_to_summarize(self, prompt):
        # print("Asking to summarize: ", prompt)
        return self._open_ai_util.chatPlusSingle(self._ASK_TO_SUMMARIZE + prompt)
