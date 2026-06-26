import streamlit as st
import pandas as pd


#etapas:
# Passo 1 - testar conjunto de dados(dataset)
# Passo 2 - criar os KPI's
# Quais informações posso extrair do conjunto de dados 
# Passo 3 - Desenvolver/programar os kpis
# Filtrar, Agrupar, Contar, Calcular, etc.....
# Passo 4 - Criar os graficos, cards
df = pd.read_csv('Salariess.csv')

df = df.rename(columns={
    "Id": "Identificador",
    "EmployeeName": "NomeDoFuncionario",
    "JobTitle": "Cargo",
    "BasePay": "SalarioBase",
    "OvertimePay": "PagamentoHorasExtras",
    "OtherPay": "OutrosPagamentos",
    "Benefits": "Beneficios",
    "TotalPay": "PagamentoTotal",
    "TotalPayBenefits": "TotalPagamentoEBeneficios",
    "Year": "Ano",
    "Notes": "Notas",
    "Agency": "Agencia",
    "Status": "Status",
})

st.set_page_config(
    page_title='Dashboard de Vendas',
    layout='wide',

)

st.sidebar.header('Filtros')

empresas = st.sidebar.selectbox(
    'Selecione o Cargo:',
    ['Todas'] #+ list(df['Cargo'].unique())

)

st.title('Apresentando o RH da Prefeitura')

st.write('Dados')

#st.dataframe(df[['Cargo','NomeDoFuncionario']])