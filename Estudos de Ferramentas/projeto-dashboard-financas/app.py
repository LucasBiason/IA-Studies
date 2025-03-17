import streamlit as st
import plotly.express as px
from transaction_loader import TransactionLoader

st.set_page_config(layout="wide")

loader = TransactionLoader("data/finances.csv")

st.title("Dashboard de Finanças Pessoais")
st.sidebar.header("Filtros")

# Definir intervalo de data
mes = st.sidebar.selectbox("Mês", loader.mounth_filters())

# Filtro de categoria
categories = loader.category_filters()
selected_categories = st.sidebar.multiselect("Filtrar por Categorias", categories, default=categories)
df_filtered = loader.filter_data(mes, selected_categories)


c1, c2 = st.columns([0.6, 0.4])

c1.subheader("Tabela de Finanças Filtradas")
c1.dataframe(df_filtered)

c2.subheader("Distribuição de Categorias")
category_distribution = df_filtered.groupby("Categoria")["Valor"].sum().reset_index()
fig = px.pie(
    category_distribution, 
    values='Valor', 
    names='Categoria', 
    hole=0.3
)
c2.plotly_chart(fig, use_container_width=True)
