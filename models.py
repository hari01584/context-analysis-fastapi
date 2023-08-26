from typing import Any, List, Union

from fastapi import FastAPI
from pydantic import BaseModel

class StringBody(BaseModel):
    text: str

class User(BaseModel):
    email: str
    password: str

class RelatedTweetItem(BaseModel):
    name: str
    text: Union[str, None] = None
    like: Union[int, None] = 10
    retweet: Union[int, None] = 10
    messages: Union[int, None] = 10

class GraphData(BaseModel):
    labels: List[str]
    values: List[int]

class ModelResult(BaseModel):
    label: str
    score: float

class OperationResult(BaseModel):
    code: int
    result: Union[str, None] = None
    message: Union[str, None] = None

class History(BaseModel):
    topic_or_sentiment: str
    tweet: str