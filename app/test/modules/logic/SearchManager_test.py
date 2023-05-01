# This class tests the SearchManager class by using the MockSearchApi class.
import unittest
from modules.logic.SearchManager import SearchManager
from modules.search.MockSearchApi import MockSearchApi


class SearchManager_test(unittest.TestCase):
    def test_search(self):
        # Initialize search APIs
        mock_search_api = MockSearchApi()

        # Initialize SearchManager with a list of search APIs
        multi_search = SearchManager()
        multi_search.add_search_api(mock_search_api)

        # Set query
        query = "python programming"

        # Define callback function
        def search_callback(results):
            for search_engine_id, result in results.items():
                print(f"Search results from {search_engine_id}:")
                print(result)

        # Run search
        multi_search.run_search(query, search_callback)
