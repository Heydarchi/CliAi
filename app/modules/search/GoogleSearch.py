import requests
import json
from api.search.AbstractSearchApi import *

class GoogleSearch(AbstractSearchApi):
    def __init__(self, api_key):
        self.api_key = api_key
        self.search_engine_id = SearchEngine.GOOGLE
        self._init_variables()

    def _init_variables(self):
        self.base_url = "https://www.google.com/search"

    def search(self, query, num_results=10):
        if self.api_key is not None:
            return self.search_by_api(query, num_results)
        else:

    def search_by_api(self, query):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.search_engine_id,
            "q": query
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error occurred while fetching search results: {response.status_code}")

    def search_scraping(self, query, num_results=10):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        params = {
            "q": query
        }
        response = requests.get(self.base_url, headers=headers, params=params)

        if response.status_code == 200:
            return self.parse_results(response.text)
        else:
            raise Exception(f"Error occurred while fetching search results: {response.status_code}")

    def parse_results(self, html):
        soup = BeautifulSoup(html, "html.parser")
        search_results = []

        for g in soup.find_all("div", class_="tF2Cxc"):
            result = {}
            title_element = g.find("h3", class_="LC20lb DKV0Md")
            link_element = g.find("a")

            if title_element and link_element:
                result["title"] = title_element.text
                result["link"] = link_element["href"]
                search_results.append(result)

        return search_results

if __main__ == "__main__":

    # Replace with your API key and search engine ID
    api_key = NONE


    # Perform a search and get the results in JSON format
    query = "example search query"
    search_results_json = google_search.search(query)

    # Print the search results as a formatted JSON string
    print(json.dumps(search_results_json, indent=2))
