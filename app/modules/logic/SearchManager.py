import threading
from modules.search.GoogleSearchApi import GoogleSearchApi
from modules.search.BingSearchApi import BingSearchApi


class SearchManager:
    def __init__(self):
        self.search_apis = []
        self.results = {}

    def add_search_api(self, search_api):
        self.search_apis.append(search_api)

    def threaded_search(self, search_api, query):
        self.results[search_api.get_search_engine_name()] = search_api.search(query)

    def run_search(self, query, callback):
        search_threads = []

        for search_api in self.search_apis:
            thread = threading.Thread(
                target=self.threaded_search, args=(search_api, query)
            )
            search_threads.append(thread)
            thread.start()

        for thread in search_threads:
            thread.join()
        # print("SearchManager results:", self.results)
        callback(self.results)


if __name__ == "__main__":
    # Initialize search APIs
    google_search_api = GoogleSearchApi(None)
    bing_search_api = BingSearchApi(None)

    # Initialize SearchManager with a list of search APIs
    multi_search = SearchManager()
    multi_search.add_search_api(google_search_api)
    multi_search.add_search_api(bing_search_api)

    # Set query

    query = "How to make a search engine in Python?"
    input_query = input("Enter your query: ")
    if input_query:
        query = input_query

    # Define callback function
    def search_callback(results):
        for search_engine_id, result in results.items():
            print(f"Search results from {search_engine_id}:")
            print(result)

    # Run search
    multi_search.run_search(query, search_callback)
