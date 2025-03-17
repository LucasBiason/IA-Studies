from fastapi import FastAPI
from .views import router
from .model import HousePricePrediction

app = FastAPI()

app.include_router(router)

classifier = HousePricePrediction()
classifier.train()