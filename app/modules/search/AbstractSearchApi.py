from dataclasses import dataclass, field
from enum import Enum
from dataclass_wizard import JSONWizard
from dataclasses import asdict


class SearchEngine(Enum):
    MOCK = -1, "MOCK"
    NOT_SET = 0, "NOT_SET"
    GOOGLE = 1, "GOOGLE"
    BING = 2, "BING"
    YAHOO = 3, "YAHOO"


@dataclass
class SearchResult(JSONWizard):
    url: str = ""
    title: str = ""
    description: str = ""

    def __repr__(self):
        return f"url={self.url}, title={self.title}, description={self.description}"

    def to_dict(self):
        return asdict(self)


class AbstractSearchApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.search_engine_id = SearchEngine.NOT_SET

    def get_search_engine_id(self):
        return self.search_engine_id

    def get_search_engine_name(self):
        return self.search_engine_id.name

    def seacrh(self):
        pass
