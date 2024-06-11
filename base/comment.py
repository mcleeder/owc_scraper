from pydantic import BaseModel, Field, root_validator
from typing import Optional, Any
from datetime import datetime


class Content(BaseModel):
    id: str
    text: str
    type: str

    @root_validator(pre=True)
    def check_text_or_description(cls, values):
        if "text" not in values and "description" in values:
            values["text"] = values.pop("description")
        return values


class Rank(BaseModel):
    ranks_up: int
    ranks_down: int
    ranked_by_current_user: int


class Comment(BaseModel):
    conversation_id: str
    id: str
    parent_id: Optional[str]
    user_id: str
    written_at: datetime
    content: list[Content]
    replies: list[Any] = Field(default_factory=list)
    depth: int
    replies_count: int
    rank: Rank


class CommentData(BaseModel):
    conversation_id: str
    root_comment: str
    id: str
    user_id: str
    written_at: datetime
    replies_count: int
    content: list[Content]
    replies: list[Comment] = Field(default_factory=list)
    rank: Rank
