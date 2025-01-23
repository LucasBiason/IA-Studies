import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# treinamento do modelo
df = pd.read_csv('pizzas.csv')
modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x, y)

# frontend
st.title("Predição de Preço de Pizza")
st.divider()
diametro = st.number_input("Digite o diâmetro da pizza em polegadas:", min_value=0.0, step=0.1)
if st.button("Prever Preço"):
    preco = modelo.predict([[diametro]])[0][0]
    st.write(f"O preço previsto para uma pizza de {diametro} polegadas é R$ {preco:.2f}")

