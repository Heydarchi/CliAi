# This class implements a mock search api. It is used for testing purposes.
from modules.search.AbstractSearchApi import *


class MockSearchApi(AbstractSearchApi):
    def __init__(self):
        self.search_engine_id = SearchEngine.MOCK

    def search(self, query, num_results=10):
        result = []
        for i in range(0, num_results):
            search_result = SearchResult()
            search_result.title = f"Title {i}"
            search_result.url = f"https://www.example.com/{i}"
            search_result.description = f"Description {i}"
            result.append(search_result)
        return result
