import enum


class SearchEngine(enum.Enum):
    NOT_SET = 0
    GOOGLE = 1
    BING = 2
    YAHOO = 3

class AbstractSearchApi(Resource):

    def __init__(self, api_key):
        self.api_key = api_key
        self.search_engine_id = SearchEngine.NOT_SET

    def get_search_engine_id(self):
        return self.search_engine_id

    def seacrh(self):
        pass
