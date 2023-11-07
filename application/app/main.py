from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
import pickle

class BodyModel(BaseModel):
    currency: str
    fee: str
    pets_allowed: str
    category: str
    cityname: str
    price_type: str
    state: str
    bathrooms: int
    bedrooms: int
    square_feet: int


app = FastAPI()

model = pickle.load(open("../../model/model.sav", "rb"))

@app.post("/predict")
async def predict(body: BodyModel):
    data = body.model_dump()
    data = pd.json_normalize(data)
    prediction = model.predict(data)
    return {"prediction": prediction[0]}

