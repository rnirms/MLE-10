from transformers import pipeline
from fastapi import FastAPI
from mangum import Mangum

from pydantic import BaseModel
from typing import List

class BodyModel(BaseModel):
    comments: List[str]
   


model_path = 'model'
classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

app = FastAPI(title='Serverless Lambda FastAPI', root_path="/Prod/")


@app.post("/sentiment", tags=["Sentiment Analysis"])
def sentiment( item: BodyModel):
    comments = item.comments
    return {'result': classify(comments)}



@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Ok"}


handler = Mangum(app=app)