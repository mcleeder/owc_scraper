from typing import Any
from base.scraper import Scraper
from base.comment import Comment
from requests import session


class Yahoo(Scraper):

    def __init__(self) -> None:
        super().__init__()

    SITE_NAME = "Yahoo"

    def get_data(url: str) -> Any:
        web = session()
        response = web.get(url)
        return response.text

    def parse_data(raw_data: Any) -> list[Comment]: ...
