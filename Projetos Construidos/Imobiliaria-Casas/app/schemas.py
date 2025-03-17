from pydantic import BaseModel

class HouseFeatures(BaseModel):
    tamanho: float
    localizacao: str
    quantidade_quartos: int

class PricePrediction(BaseModel):
    price: float