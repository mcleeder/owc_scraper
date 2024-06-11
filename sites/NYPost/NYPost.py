from typing import Any
from base.scraper import Scraper
from base.comment import Comment


class NYPost(Scraper):

    SITE_NAME = "NYPost"

    SPOT_ID = "sp_Sx8YukwE"

    def get_data(url: str) -> Any: ...

    def parse_data() -> list[Comment]: ...
