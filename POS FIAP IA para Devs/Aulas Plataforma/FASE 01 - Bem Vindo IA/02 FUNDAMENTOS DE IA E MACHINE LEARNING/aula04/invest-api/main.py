from fastapi import FastAPI
from routers import data, calculations

app = FastAPI()

app.include_router(data.router)
app.include_router(calculations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the InvestPy API"}