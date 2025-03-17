from fastapi import APIRouter, HTTPException
from .schemas import HouseFeatures, PricePrediction
from .model import HousePricePrediction

router = APIRouter()

model = HousePricePrediction()

@router.post("/predict", response_model=PricePrediction)
def predict(features: HouseFeatures):
    try:
        prediction = model.predict([features.tamanho, features.localizacao, features.quantidade_quartos])
        return {"price": prediction}
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))