from base.scraper import Scraper
from utils.lightscraper import LightElement


class Yahoo(Scraper):

    SITE_NAME = "Yahoo"

    SPOT_ID = "sp_Rba9aFpG"

    def _get_post_id(self, html_tree: LightElement) -> str:
        button = html_tree.element("//button[@data-uuid]")
        return button.attrib.get("data-uuid")
