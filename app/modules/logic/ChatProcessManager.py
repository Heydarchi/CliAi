import threading
from modules.search.GoogleSearchApi import GoogleSearchApi
from modules.search.BingSearchApi import BingSearchApi
from modules.ai.ChatGpt import ChatGpt
from modules.web.WebScrapper import WebScrapper
from modules.logic.SearchManager import SearchManager
from modules.utility.ChatGptResponseParser import *
from json import dumps
import json


class ChatSearchManager:
    def __init__(self):
        self.chat_gpt = ChatGpt()
        self.search_manager = SearchManager()
        self.scraper = WebScrapper()
        self.chat_response_parser = ChatGptResponseParser()
        self._init_search_manager()

    def _init_search_manager(self):
        google_search_api = GoogleSearchApi(None)
        bing_search_api = BingSearchApi(None)
        # self.search_manager.add_search_api(google_search_api)
        self.search_manager.add_search_api(bing_search_api)

    def search_callback(self, results):
        try:
            # print("\n\nCallback is invkoed! Search results:", results)
            converted_results = self.convert_search_results_to_json(results)
            # print("\n\nConverted results: " + converted_results)
            selected_links = self.chat_gpt.select_links_to_scrap(converted_results)
            the_links = self.chat_response_parser.extract(
                selected_links, EXTRACT_TAGS.LINKS.name
            )
            # print("\n\nSelected links:", the_links)
            scrapped_contents = self.scraper.scrap_links(the_links)

            summarized_contents = []
            # print("\n\nScrapped contents[0]:", type(scrapped_contents[0]), scrapped_contents[0]['content'])
            print("\n\n*****type of scrapped_contents:", type(scrapped_contents))
            for content in scrapped_contents:
                print("\n\n*****type of content[content]:", type(content["content"]))
                prompt = []
                if len(content["content"]) > 16000:
                    prompt.append(content["content"][:16000])
                    prompt.append(content["content"][16000:])
                result = ""
                for p in prompt:
                    result = result + " " + self.chat_gpt.ask_to_summarize(p)
                summarized_contents.append(result)
            # print("\n\nSummarized contents:", summarized_contents)
            print("\n\n*******type of summarized_contents:", type(summarized_contents))
            formatted_output = self.chat_gpt.process_scrapped_data(summarized_contents)

            print("Final response:")
            print(formatted_output)
        except Exception as e:
            print(f"An error occurred during processing: {e}")

    def get_recommended_keywords(self, user_request):
        try:
            return self.chat_gpt.ask_for_keywords(user_request)
        except Exception as e:
            print(f"An error occurred while getting recommended keywords: {e}")
            return None

    def process_request(self, user_request):
        recommended_keywords = self.get_recommended_keywords(user_request)
        print("Recommended keywords:", recommended_keywords)
        if recommended_keywords:
            self.search_manager.run_search(recommended_keywords, self.search_callback)
        else:
            print("Could not process request due to missing recommended keywords.")

    def convert_search_results_to_json(self, search_results):
        # print("type of search_results:", type(search_results))
        lst_results = []
        for key, value in search_results.items():
            for item in value:
                # print("\nType of item:", type(item))
                lst_results.append(item)
        # Convert SearchResult objects to dictionaries
        lst_results_dicts = [result.to_dict() for result in lst_results]

        # Convert the list of dictionaries to a JSON string
        json_string = json.dumps(lst_results_dicts)

        return json_string


if __name__ == "__main__":
    # Initialize GPTSearchManager
    gpt_search_manager = ChatSearchManager()

    query = "How to make a search engine in Python?"
    input_query = input("Enter your query: ")
    if input_query:
        query = input_query

    # Process user request
    gpt_search_manager.process_request(query)
