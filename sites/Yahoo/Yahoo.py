from typing import Any
from base.scraper import Scraper
from base.comment import Comment


class Yahoo(Scraper):

    SITE_NAME = "Yahoo"
    BASE_URL: str

    def get_data(self, url: str) -> Any: ...

    def parse_data(self) -> list[Comment]: ...
