import requests
from bs4 import BeautifulSoup
from modules.search.AbstractSearchApi import *


class BingSearchApi(AbstractSearchApi):
    def __init__(self, api_key):
        self.api_key = api_key
        self.search_engine_id = SearchEngine.BING
        self._init_variables()

    def _init_variables(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        self.base_url = "https://www.bing.com/search"

    def search(self, query, num_results=10):
        params = {"q": query, "count": num_results}
        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return self.extract_results(soup)
        else:
            raise Exception(
                f"Error occurred while fetching search results: {response.status_code}"
            )

    def extract_results(self, soup):
        lst_result = []
        for result in soup.find_all("li", class_="b_algo"):
            title_element = result.find("h2")
            link_element = title_element.find("a", href=True) if title_element else None
            snippet_element = result.find("div", class_="b_caption")

            if link_element and snippet_element:
                search_result = SearchResult()
                search_result.title = title_element.text
                search_result.url = link_element["href"]
                search_result.description = snippet_element.get_text(
                    separator=" "
                ).strip()
                lst_result.append(search_result)
                """results.append({
                    "title": title_element.text,
                    "link": link_element["href"],
                    "snippet": snippet_element.get_text(separator=" ").strip()
                })"""
        return lst_result


if __name__ == "__main__":
    # Create a BingSearchApi instance
    bing_search = BingSearchApi(None)

    # Search for a query and get the results
    query = "python programming"
    results = bing_search.search(query, num_results=10)

    # Print the search results
    import json

    print(results)
