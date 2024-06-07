from typing import Any
from base.comment import Comment


class Scraper:

    COMMENTS_URL = "https://api-2-0.spot.im/v1.0.0/conversation/read"

    def get_data(url: str) -> Any:
        """
        Get Raw Data
        """
        ...

    def parse_data(raw_data: Any) -> list[Comment]:
        """
        Parse Data
        """
        ...
