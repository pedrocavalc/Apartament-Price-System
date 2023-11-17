from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
import pickle
import mlflow 

mlflow.set_tracking_uri("http://localhost:5000")
client = mlflow.tracking.MlflowClient()
model_metadata = client.get_latest_versions('Teste', stages=['Production'])
model = mlflow.sklearn.load_model(model_uri=model_metadata[0].source)

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


@app.post("/predict")
async def predict(body: BodyModel):
    data = body.model_dump()
    data = pd.json_normalize(data)
    prediction = model.predict(data)
    return {"prediction": prediction[0]}

