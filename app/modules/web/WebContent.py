import requests


class WebContent:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }

    def fetch_content(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(
                f"Error occurred while fetching content: {response.status_code}"
            )


if __name__ == "__main__":
    web_content = WebContent()
    html = web_content.fetch_content("https://www.time.is")
    print(html)
