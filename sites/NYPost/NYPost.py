from base.scraper import Scraper
from utils.lightscraper import LightElement


class Nypost(Scraper):

    SITE_NAME = "Nypost"

    SPOT_ID = "sp_Sx8YukwE"

    def _get_post_id(self, html: LightElement) -> str:
        element = html.element("//div[@data-post-id]")
        return element.attrib["data-post-id"]
