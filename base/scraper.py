from datetime import datetime
import json

from requests import session
from base.comment import Comment, CommentData, Content, Rank
from utils.lightscraper import LightElement


class Scraper:

    COMMENTS_URL = "https://api-2-0.spot.im/v1.0.0/conversation/read"
    SITE_NAME = None

    # SPOT_ID is static(?) site id for OpenWeb
    # Ex- sp_Rba9aFpG
    SPOT_ID = None

    PAYLOAD = {
        "sort_by": "best",
        "offset": 0,
        "count": 100,
        "message_id": None,
        "depth": 4,
        "child_count": 10,
    }

    def get_data(self, url: str) -> dict:
        """
        Get Data
        """
        web = session()

        response = web.get(url)
        html_tree = LightElement(response.text)

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",  # noqa: E501
            "x-post-id": None,
            "x-spot-id": self.SPOT_ID,
        }

        headers["x-post-id"] = self._get_post_id(html_tree)

        # Sets session cookie auth token
        _ = web.post(url="https://api-2-0.spot.im/v1.0.0/authenticate", headers=headers)

        raw_comments = web.post(
            url="https://api-2-0.spot.im/v1.0.0/conversation/read",
            headers=headers,
            json=self.PAYLOAD,
        )

        return json.loads(raw_comments.text)["conversation"]["comments"]

    def _get_post_id(self, html_tree: LightElement) -> str:
        """
        Parse site page to find post_id attribute (article id)
        Implement for child sites
        """
        ...

    def parse_data(self, json_data: dict) -> list[CommentData]:
        comments_data = []
        for comment in json_data:
            filtered_content = self._filter_content(comment["content"])
            comment_obj = CommentData(
                conversation_id=comment["conversation_id"],
                root_comment=comment["root_comment"],
                id=comment["id"],
                user_id=comment["user_id"],
                written_at=datetime.fromtimestamp(comment["written_at"]),
                replies_count=comment["replies_count"],
                content=[Content(**content) for content in filtered_content],
                replies=self._parse_replies(comment.get("replies", [])),
                rank=Rank(**comment["rank"]),
            )

            comments_data.append(comment_obj)
        return comments_data

    def _filter_content(self, content: list[dict]) -> list[dict]:
        """
        We sometimes get comments wrapped in user-mentions and context ads
        """
        return [c for c in content if all([c.get("id"), c.get("text")])]

    def _parse_replies(self, replies: list[dict]) -> list[Comment]:
        comments = []
        for reply in replies:
            comment = Comment(
                conversation_id=reply["conversation_id"],
                id=reply["id"],
                parent_id=reply.get("parent_id"),
                user_id=reply["user_id"],
                written_at=datetime.fromtimestamp(reply["written_at"]),
                content=[Content(**content) for content in reply.get("content", "")],
                replies=self._parse_replies(reply.get("replies", [])),
                depth=reply["depth"],
                replies_count=reply["replies_count"],
                rank=Rank(**reply["rank"]),
            )
            comments.append(comment)
        return comments
