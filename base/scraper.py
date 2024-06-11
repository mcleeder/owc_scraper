from typing import Any
from base.comment import Comment
from utils.lightscraper import LightElement


class Scraper:

    COMMENTS_URL = "https://api-2-0.spot.im/v1.0.0/conversation/read"
    SITE_NAME = None
    SPOT_ID = None

    PAYLOAD = {
        "sort_by": "best",
        "offset": 0,
        "count": 100,
        "message_id": None,
        "depth": 4,
        "child_count": 10,
    }

    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",  # noqa: E501
        "x-post-id": None,
        "x-spot-id": SPOT_ID,
    }

    def get_data(url: str) -> Any:
        """
        Get Raw Data
        """
        ...

    def _get_spot_id(html: LightElement) -> str: ...

    def parse_data(raw_data: Any) -> list[Comment]:
        """
        Parse Data
        """
        ...
