from typing import Any
from comment import Comment

class Scraper():
    SITE_NAME: str
    BASE_URL: str

    def get_data(self, url: str) -> Any:
        """
        Get Raw Data
        """
        ...
    
    def parse_data(self) -> list[Comment]:
        """
        Parse Data
        """
        ...