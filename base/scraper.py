from typing import Any
from base.comment import Comment


class Scraper:

    def __init__(self) -> None:
        pass

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
