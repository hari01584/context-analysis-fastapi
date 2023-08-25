from fastapi import FastAPI
from transformers import pipeline
import numpy as np
import pandas as pd
import pickle
import re
import gsdmm.gsdmm
from gsdmm.gsdmm import MovieGroupProcess
from tqdm import tqdm
import gensim
from gensim.models import CoherenceModel

from typing import Any, List, Union

from models import RelatedTweetItem

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict_topic")
async def predict_topic(text: str):
    print(text)
    # Load the model
    mgp = pickle.load(open('chunk6_STTM.sav', 'rb'))
    topic_label, score = mgp.choose_best_label(text)
    return {"message": topic_label, "score": score}


@app.get("/related_tweet", response_model=List[RelatedTweetItem])
async def dummy_related_tweet(tweetTopic: str = None) -> Any:
    print ("Dummy return for", tweetTopic)
    return [
        {"name": "Abhinandan", "text": "A sample tweet"},
        {"name": "Sahil", "text": "A aaaaaa tweet"},
    ]