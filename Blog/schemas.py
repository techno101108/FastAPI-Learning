from pydantic import BaseModel
from typing import Optional


class create_post(BaseModel):
    title: str
    content: str
    # to create optional field
    published: bool = True
    # to create optional field- >none
    rating: Optional[int] = None
