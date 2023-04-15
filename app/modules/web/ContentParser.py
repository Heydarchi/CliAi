import requests
from bs4 import BeautifulSoup


class ContentParser:
    def extract_meta_tags(self, soup):
        meta_tags = {}
        for meta in soup.find_all("meta"):
            name = meta.get("name") or meta.get("property")
            content = meta.get("content")
            if name and content:
                meta_tags[name] = content
        return meta_tags

    def extract_links(self, soup):
        return [a["href"] for a in soup.find_all("a", href=True)]

    def extract_images(self, soup):
        return [img["src"] for img in soup.find_all("img", src=True)]

    def parse(self, html):
        soup = BeautifulSoup(html, "html.parser")
        info = {}

        # Extract the page title
        title_element = soup.find("title")
        if title_element:
            info["title"] = title_element.text

        # Extract meta tags
        info["meta_tags"] = self.extract_meta_tags(soup)

        # Extract headings (h1, h2, h3, h4, h5, h6)
        headings = []
        for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            headings.extend(soup.find_all(tag))
        info["headings"] = [heading.text for heading in headings]

        # Extract links
        info["links"] = self.extract_links(soup)

        # Extract images
        info["images"] = self.extract_images(soup)

        # Extract the main text content
        content_element = soup.find("body")
        if content_element:
            info["content"] = content_element.get_text(separator=" ").strip()

        return info


if __name__ == "__main__":
    content_parser = ContentParser()
    html = requests.get("https://www.google.com").text
    print(content_parser.parse(html))
