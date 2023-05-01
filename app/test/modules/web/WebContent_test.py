# This is a test file for the WebContent class
import unittest
from modules.web.WebContent import WebContent


class WebContent_test(unittest.TestCase):
    def test_fetch_content(self):
        web_content = WebContent()
        html = web_content.fetch_content("https://www.time.is")
        print(html)
        self.assertTrue("Time.is" in html)
