import requests
import json
from modules.search.AbstractSearchApi import *
from bs4 import BeautifulSoup
from googlesearch import search


class GoogleSearchApi(AbstractSearchApi):
    def __init__(self, api_key):
        self.api_key = api_key
        self.search_engine_id = SearchEngine.GOOGLE
        self._init_variables()

    def _init_variables(self):
        self.base_url = "https://www.google.com/search"

    def search(self, query, num_results=10):
        return self.search_by_api(query)
        """if self.api_key is not None:
        else:
            return self.search_scraping(query, num_results)"""

    def search_by_api(self, query):
        result = search(query, num_results=10, advanced=True)
        lst_result = []
        for item in result:
            search_result = SearchResult()
            search_result.title = item.title
            search_result.url = item.url
            search_result.description = item.description
            lst_result.append(search_result)
        return lst_result

    def search_scraping(self, query, num_results=10):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        params = {"q": query}
        response = requests.get(self.base_url, headers=headers, params=params)

        if response.status_code == 200:
            return self.parse_results(response.text)
        else:
            raise Exception(
                f"Error occurred while fetching search results: {response.status_code}"
            )

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


if __name__ == "__main__":
    google_search = GoogleSearchApi("")
    results = google_search.search("python")
    print(results)
