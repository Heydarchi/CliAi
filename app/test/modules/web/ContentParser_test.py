import unittest
from modules.web.ContentParser import ContentParser
from bs4 import BeautifulSoup


class ContentParser_test(unittest.TestCase):
    def test_extract_meta_tags(self):
        content_parser = ContentParser()
        html = """
        <html>
            <head>
                <meta name="description" content="This is a description">
                <meta property="og:title" content="This is an og:title">
            </head>
            <body>
                <p>Some content</p>
            </body>
        </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        meta_tags = content_parser.extract_meta_tags(soup)
        self.assertEqual(meta_tags["description"], "This is a description")
        self.assertEqual(meta_tags["og:title"], "This is an og:title")

    def test_extract_links(self):
        content_parser = ContentParser()
        html = """
        <html>
            <head></head>
            <body>
                <p>Some content</p>
                <a href="https://www.google.com">Google</a>
                <a href="https://www.yahoo.com">Yahoo</a>
            </body>
        </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        links = content_parser.extract_links(soup)
        self.assertEqual(links[0], "https://www.google.com")
        self.assertEqual(links[1], "https://www.yahoo.com")

    def test_extract_images(self):
        content_parser = ContentParser()
        html = """
        <html>
            <head></head>
            <body>
                <p>Some content</p>
                <img src="https://www.google.com/logo.png">
                <img src="https://www.yahoo.com/logo.png">
            </body>
        </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        images = content_parser.extract_images(soup)
        self.assertEqual(images[0], "https://www.google.com/logo.png")
        self.assertEqual(images[1], "https://www.yahoo.com/logo.png")

    def test_parse(self):
        content_parser = ContentParser()
        html = """
        <html>
            <head>
                <title>This is a title</title>
                <meta name="description" content="This is a description">
                <meta property="og:title" content="This is an og:title">
            </head>
            <body>
                <h1>Heading 1</h1>
                <h2>Heading 2</h2>
                <p>Some content</p>
                <a href="https://www.google.com">Google</a>
                <a href="https://www.yahoo.com">Yahoo</a>
                <img src="https://www.google.com/logo.png">
                <img src="https://www.yahoo.com/logo.png">
                <p>Extra info!</p>
            </body>
        </html>
        """
        info = content_parser.parse(html)
        self.assertEqual(info["title"], "This is a title")
        self.assertEqual(info["meta_tags"]["description"], "This is a description")
        self.assertEqual(info["meta_tags"]["og:title"], "This is an og:title")
        self.assertEqual(info["headings"][0], "Heading 1")
        self.assertEqual(info["headings"][1], "Heading 2")
        self.assertEqual(info["links"][0], "https://www.google.com")
        self.assertEqual(info["links"][1], "https://www.yahoo.com")
        self.assertEqual(info["images"][0], "https://www.google.com/logo.png")
        self.assertEqual(info["images"][1], "https://www.yahoo.com/logo.png")
        print(info["content"])
        self.assertEqual(
            info["content"],
            "Heading 1 \n Heading 2 \n Some content \n Google \n Yahoo \n \n \n Extra info!",
        )
