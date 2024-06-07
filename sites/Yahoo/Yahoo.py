from typing import Any
from base.scraper import Scraper
from base.comment import Comment
from requests import session


class Yahoo(Scraper):

    SITE_NAME = "Yahoo"

    payload = {
        "child_count": 2,
        "coversation_id": "",
        "count": 25,
        "depth": 2,
        "offset": 3,
        "sort_by": "best",
    }

    headers = {}

    def get_data(url: str) -> Any:
        web = session()
        response = web.get(url)
        return response.text

    def parse_data(raw_data: Any) -> list[Comment]: ...
