from base.scraper import Scraper
from utils.lightscraper import LightElement


class NYPost(Scraper):

    SITE_NAME = "NYPost"

    SPOT_ID = "sp_Sx8YukwE"

    def _get_post_id(self, html: LightElement) -> str: ...
