#Importar as bibliotecas
import datetime
import sqlite3

import pandas as pd
from datetime import date
import streamlit as st
import datetime as dt
import numpy as np

#Ler e tratar dados
conn = sqlite3.connect('banco_acoes.db')
df = pd.read_sql('SELECT * FROM acoes', con=conn)
conn.close()

df.drop(columns=['index'], inplace=True)
df['Data'] = pd.to_datetime(df['Data'])


st.header('WebApp Ações')

st.subheader('Visualizar ações')

acoes = df.columns[1:]

st.sidebar.header('Parâmetros')
choice_acoes = st.sidebar.multiselect('Selecione a sua ação', acoes)

data = pd.to_datetime(df['Data'])
min_data = pd.to_datetime(min(data))
max_data = pd.to_datetime(max(data))

data_start = st.sidebar.date_input('Data inicial', min_data)
data_end = st.sidebar.date_input('Data final', max_data)

start = pd.to_datetime(data_start)
end = pd.to_datetime(data_end)

intervalo_data = df[(df['Data'] >= start) & (df['Data'] <= end)]
intervalo_data = intervalo_data.set_index('Data')

dados = intervalo_data[choice_acoes]

if data_end < data_start:
    st.error('Data inicial maior que data final')

if len(choice_acoes) > 0:
    st.line_chart(dados)

