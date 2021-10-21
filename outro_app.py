#Importar as bibliotecas
import datetime
import yfinance as yf
import pandas as pd
from datetime import date
import streamlit as st
import datetime as dt
import numpy as np

#Ler e tratar dados
dados = r'C:\Users\mathe\Desktop\Projeto23\App\Tabela_ações.csv'
df = pd.read_csv(dados)
df = df.dropna()



st.header('WebApp Ações')

st.subheader('Visualizar ações')

acoes = df.columns[:(len(df.columns) - 1)]

st.sidebar.header('Parâmetros')
choice_acoes = st.sidebar.multiselect('Selecione a sua ação', acoes)

data = pd.to_datetime(df['Data'])
#min_data = pd.to_datetime(min(data))
#max_data = pd.to_datetime(max(data))

data_start = st.sidebar.date_input("Data inicial", value = pd.to_datetime('01-01-2010'))
data_end = st.sidebar.date_input("Data final", value = pd.to_datetime('today'))

start = pd.to_datetime(data_start).date()
end = pd.to_datetime(data_end).date()


if data_end < data_start:
    st.error('Data inicial maior que data final')

if len(choice_acoes) > 0:
    stock = yf.download(choice_acoes, start=start, end=end)
    st.line_chart(stock['Adj Close'])

    fechamento = stock['Adj Close']


    #stock_normalizado = stock.copy()
    #for i in stock_normalizado:
    #    stock_normalizado = np.log(stock['Adj Close'][len(stock)-1] / stock['Adj Close'][0])
    #    stock_normalizado = pd
    #    st.dataframe(stock_normalizado)






#Visualização de dados