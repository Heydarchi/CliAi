from dataclasses import dataclass, field
from enum import Enum
from dataclass_wizard import JSONWizard


class SearchEngine(Enum):
    NOT_SET = 0
    GOOGLE = 1
    BING = 2
    YAHOO = 3


@dataclass
class SearchResult(JSONWizard):
    url: str = ""
    title: str = ""
    description: str = ""

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


class AbstractSearchApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.search_engine_id = SearchEngine.NOT_SET

    def get_search_engine_id(self):
        return self.search_engine_id

    def seacrh(self):
        pass
