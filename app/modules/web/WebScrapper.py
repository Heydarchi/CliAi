# This class utilizes WebContent & ContentProcess to fetch link content and process it to get the required output
from modules.web.WebContent import WebContent
from modules.web.ContentParser import ContentParser


class WebScrapper:
    def __init__(self):
        self.web_content = WebContent()
        self.content_parser = ContentParser()

    def scrap_links(self, links):
        scrapped_contents = []
        for link in links:
            html = self.web_content.fetch_content(link)
            scrapped_contents.append(self.content_parser.parse(html))

        return scrapped_contents


if __name__ == "__main__":
    content_scraper = ContentScraper()
    scrapped_contents = content_scraper.scrap_links(
        ["https://www.time.is", "https://www.google.com", "https://www.bing.com"]
    )
    print(scrapped_contents)
