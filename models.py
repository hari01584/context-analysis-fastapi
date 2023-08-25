from typing import Any, List, Union

from fastapi import FastAPI
from pydantic import BaseModel

class RelatedTweetItem(BaseModel):
    name: str
    text: Union[str, None] = None
    like: Union[int, None] = 10
    retweet: Union[int, None] = 10
    messages: Union[int, None] = 10