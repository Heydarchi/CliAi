import unittest
from modules.utility.ChatGptResponseParser import ChatGptResponseParser


class ChatGptResponseParser_test(unittest.TestCase):
    def test_extract_links(self):
        chat_gpt_response_parser = ChatGptResponseParser()
        response = '!!LINKS!!=["https://www.youtube.com/watch?v=6ZfuNTqbHE8", "https://www.youtube.com/watch?v=6ZfuNTqbHE8", "https://www.youtube.com/watch?v=6ZfuNTqbHE8"]'
        links = chat_gpt_response_parser.extract(response, "LINKS")
        self.assertEqual(len(links), 3)
        self.assertEqual(links[0], "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
        self.assertEqual(links[1], "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
        self.assertEqual(links[2], "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

    def test_extract_content(self):
        chat_gpt_response_parser = ChatGptResponseParser()
        response = '!!CONTENT!!=["This is some content"]'
        content = chat_gpt_response_parser.extract(response, "CONTENT")
        self.assertEqual(content, ["This is some content"])

    def test_extract_code(self):
        chat_gpt_response_parser = ChatGptResponseParser()
        response = '!!CODE!!=["the_provided_code"]'
        code = chat_gpt_response_parser.extract(response, "CODE")
        self.assertEqual(code, ["the_provided_code"])

    def test_extract_file(self):
        chat_gpt_response_parser = ChatGptResponseParser()
        response = '!!FILE!!=["the_provided_file"]'
        file = chat_gpt_response_parser.extract(response, "FILE")
        self.assertEqual(file, ["the_provided_file"])

    def test_extract_keywords(self):
        chat_gpt_response_parser = ChatGptResponseParser()
        response = '!!KEYWORDS!!=["the_provided_keywords"]'
        keywords = chat_gpt_response_parser.extract(response, "KEYWORDS")
        self.assertEqual(keywords, ["the_provided_keywords"])

    def test_extract_shell_script(self):
        chat_gpt_response_parser = ChatGptResponseParser()
        response = '!!SHELL_SCRIPT!!=["Content_1", "Content2", "Content3"]'
        shell_script = chat_gpt_response_parser.extract(response, "SHELL_SCRIPT")
        self.assertEqual(shell_script, ["Content_1", "Content2", "Content3"])

    def test_extract_all(self):
        chat_gpt_response_parser = ChatGptResponseParser()
        response = """
        !!SHELL_SCRIPT!!=["Content_1", "Content2", "Content3"]
        !!CODE!!=["the_provided_code"]
        !!FILE!!=["the_provided_file"]
        !!CONTENT!!=["the_provided_content"]
        !!LINKS!!=["Link_1", "Link2", "Link3"]
        !!KEYWORDS!!=["the_provided_keywords"]
        """
        extracted_data = chat_gpt_response_parser.extract_all(response)
        self.assertEqual(
            extracted_data["shell_script"], ["Content_1", "Content2", "Content3"]
        )
        self.assertEqual(extracted_data["code"], ["the_provided_code"])
        self.assertEqual(extracted_data["file"], ["the_provided_file"])
        self.assertEqual(extracted_data["content"], ["the_provided_content"])
        self.assertEqual(extracted_data["links"], ["Link_1", "Link2", "Link3"])
        self.assertEqual(extracted_data["keywords"], ["the_provided_keywords"])
