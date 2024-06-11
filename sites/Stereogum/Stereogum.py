from base.scraper import Scraper
from utils.lightscraper import LightElement


class Stereogum(Scraper):

    SITE_NAME = "Stereogum"

    # SPOT_ID is static(?) site id for OpenWeb
    # Ex- sp_Rba9aFpG
    SPOT_ID = "sp_J3wyckM8"

    def _get_post_id(self, html_tree: LightElement) -> str:
        element = html_tree.element("//*[@data-post-id]")
        return element.attrib.get("data-post-id")
