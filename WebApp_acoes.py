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

#df.drop(columns=['index'], inplace=True)
df['Data'] = pd.to_datetime(df['Data'])


st.header('WebApp Ações')

st.write("""
**Seja bem vindo(a) ao WebApp_acões!**

Ele foi desenvolvido por ***Matheus Zanetti*** para que você tenha uma visão do comportamento das ações que compõe o *BOVA11* desde de o ano de 2010.

Na barra ao lado você pode escolher a(s) ação(ões) e o intervalo de tempo desejado.

**Aproveite!**  
""")

acoes = df.columns[1:]

st.sidebar.header('Selecione os parâmetros de sua pesquisa')
choice_acoes = st.sidebar.multiselect('Selecione a(s) sua(s) ação(es)', acoes)


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

dados_nomalizado = dados.copy()
for i in dados_nomalizado.columns:
    dados_nomalizado[i] = (dados_nomalizado[i]/dados_nomalizado[i][0])

if data_end < data_start:
    st.error('Data inicial maior que data final')

if len(choice_acoes) > 0:
    st.subheader('Preço(s) dos papéis das ação(es)')
    st.write('Nesse gráfico você encontrará a evolução dos preço(s) dos papel(éis) selecionada(s)')
    st.line_chart(dados)

if len(choice_acoes) > 0:
    st.subheader('Taxa(s) de retorno do(s) investimento(s) das ação(ões) selecionada(s)')
    st.write('Nesse gráfico você encontrará a(s) taxa(s) de retorno das ação(ões) selecionada(s)')
    st.line_chart(dados_nomalizado)

