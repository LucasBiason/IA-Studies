from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import investpy.dados as dados
import investpy.calculos as calculos
import pandas as pd

router = APIRouter()

class StockRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    api_key: str

@router.post("/indicators/")
def calculate_indicators(request: StockRequest):
    try:
        df = dados.obter_dados_acao(request.ticker, request.api_key)
        # Filtrar os dados de acordo com as datas fornecidas
        df_filtered = df[(df['data'] >= request.start_date) & (df['data'] <= request.end_date)]
        df_with_indicators = calculos.calcular_retorno_diario(df_filtered)
        return {"retorno_diario": df_with_indicators.to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))