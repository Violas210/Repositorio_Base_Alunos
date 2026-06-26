import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Compras.csv', sep=';')

st.set_page_config(page_title='Dashboard - Vendas')

st.sidebar.header('Filtros')
st.title('Vendas por regiões')

maisCompr = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head()


grafico1 = plt.figure(figsize=(10,5))
plt.barh(maisCompr.index,maisCompr.values)
plt.tight_layout()

st.pyplot(grafico1)