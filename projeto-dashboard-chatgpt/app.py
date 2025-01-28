import os
import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.title('Dashboard Call Center Atendimento ao Cliente')

df = pd.read_csv('Call Center Data.csv')
df['Answer Rate'] = df['Answer Rate'].str.replace('%', '').astype(float)

incoming_avg = df['Incoming Calls'].mean()
answered_avg = df['Answered Calls'].mean()
answer_rate_avg = df['Answer Rate'].mean()

col1, col2, col3 = st.columns(3)
col1.metric('Incoming Calls AVG', round(incoming_avg, 2))
col2.metric('Answered Calls AVG', round(answered_avg, 2))
col3.metric('Answer Rate AVG', round(answer_rate_avg, 2))

st.line_chart(df[['Incoming Calls', 'Answered Calls']])


lista_mensagens = [
    {"role": "user", "content": """O dataset a seguir corresponde a
    metricas de negócio de uma operação de suporte.
    Me informe 5 insights sobre este dataset"""}
]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)
resposta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=lista_mensagens,
)
st.markdown(resposta.choices[0].message.content)