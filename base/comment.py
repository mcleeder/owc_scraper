from datetime import datetime
from pydantic import BaseModel

class Comment(BaseModel):
    name: str
    text: str
    date: datetime
    vote_count: int
