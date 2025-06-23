from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import investpy.dados as dados

router = APIRouter()

class StockRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    api_key: str

@router.post("/historical_data/")
def get_historical_data(request: StockRequest):
    try:
        df = dados.obter_dados_acao(request.ticker, request.api_key)
        # Filtrar os dados de acordo com as datas fornecidas
        df_filtered = df[(df['data'] >= request.start_date) & (df['data'] <= request.end_date)]
        return df_filtered.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))