import re
import json
import ast
from enum import Enum


class EXTRACT_TAGS(Enum):
    SHELL_SCRIPT = "SHELL_SCRIPT"
    CODE = "CODE"
    FILE = "FILE"
    CONTENT = "CONTENT"
    LINKS = "LINKS"
    KEYWORDS = "KEYWORDS"
    DESCRIPTION = "DESCRIPTION"


class ChatGptResponseParser:
    def extract_all(self, content):
        extracted_data = {}

        for tag in EXTRACT_TAGS:
            extracted_data[tag.name] = self.extract(
                content.replace(",]", "]").replace("'", " "), tag.name
            )

        return extracted_data

    def extract(self, content, tag):
        pattern = rf"!!{tag}!!=(\[[^\]]+\])"
        match = re.search(pattern, content)
        # print("tag", tag)
        if match:
            extracted_data = match.group(1)
            extracted_data = extracted_data.replace(
                "'", '"'
            )  # Replace single quotes with double quotes
            return json.loads(extracted_data)
        return []


if __name__ == "__main__":
    # Example usage
    content = """
    !!SHELL_SCRIPT!!=["Content_1", "Content2", "Content3"]
    !!CODE!!=["the_provided_code"]
    !!FILE!!=["the_provided_file"]
    !!CONTENT!!=["the_provided_content"]
    !!DESCRIPTION!!=["the_provided_description"]
    !!LINKS!!=["Link_1", "Link2", "Link3"]
    !!KEYWORDS!!=["the_provided_keywords"]
    """

    extractor = ContentExtractor()
    extracted_data = extractor.extract_all(content)

    print("Shell scripts:", extracted_data["shell_script"])
    print("Code:", extracted_data["code"])
    print("Files:", extracted_data["file"])
    print("Content:", extracted_data["content"])
    print("Links:", extracted_data["links"])
    print("Keywords:", extracted_data["keywords"])
