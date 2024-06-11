from base.scraper import Scraper
from base.comment import CommentData, Comment, Content, Rank
from requests import session
from utils.lightscraper import LightElement
import json
from datetime import datetime


class Yahoo(Scraper):

    SITE_NAME = "Yahoo"

    SPOT_ID = "sp_Rba9aFpG"

    def get_data(self, url: str) -> dict:
        web = session()

        response = web.get(url)
        html_tree = LightElement(response.text)

        button = html_tree.element("//button[@data-uuid]")
        self.HEADERS["x-post-id"] = button.attrib.get("data-uuid")

        # Sets session cookie auth token
        _ = web.post(
            url="https://api-2-0.spot.im/v1.0.0/authenticate", headers=self.HEADERS
        )

        raw_comments = web.post(
            url="https://api-2-0.spot.im/v1.0.0/conversation/read",
            headers=self.HEADERS,
            json=self.PAYLOAD,
        )

        return json.loads(raw_comments.text)["conversation"]["comments"]

    def parse_data(self, json_data: dict) -> list[CommentData]:
        comments_data = []
        for comment in json_data:
            comment_obj = CommentData(
                conversation_id=comment["conversation_id"],
                root_comment=comment["root_comment"],
                id=comment["id"],
                user_id=comment["user_id"],
                written_at=datetime.fromtimestamp(comment["written_at"]),
                replies_count=comment["replies_count"],
                content=[Content(**content) for content in comment["content"]],
                replies=self._parse_replies(comment.get("replies", [])),
                rank=Rank(**comment["rank"]),
            )
            comments_data.append(comment_obj)
        return comments_data

    def _parse_replies(self, replies: list[dict]) -> list[Comment]:
        comments = []
        for reply in replies:
            comment = Comment(
                conversation_id=reply["conversation_id"],
                id=reply["id"],
                parent_id=reply.get("parent_id"),
                user_id=reply["user_id"],
                written_at=datetime.fromtimestamp(reply["written_at"]),
                content=[Content(**content) for content in reply["content"]],
                replies=self._parse_replies(reply.get("replies", [])),
                depth=reply["depth"],
                replies_count=reply["replies_count"],
                rank=Rank(**reply["rank"]),
            )
            comments.append(comment)
        return comments
