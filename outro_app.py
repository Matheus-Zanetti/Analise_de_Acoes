import streamlit as st
import pandas as pd
import investpy as ip
from datetime import datetime, timedelta
import plotly.graph_objs as go

countries = ['brazil', 'united states']
interval = ['Daily', 'Weekly', 'Monthly']

start_date = datetime.today() - timedelta(days=30)
end_date = datetime.today()

@st.cache
def consultar_acao(stock, country, from_date, to_date, interval):
    df = ip.get_stock_historical_data(stock=stock, country=country, from_date=from_date, to_date=to_date, interval=interval)
    return df

def format_date(dt, format='%d/%m/%Y'):
    return dt.strftime(format)

def plotCandleStick(df, acao='ticket'):
    tracel = {
        'x': df.index,
        'open': df.Open,
        'close': df.Close,
        'high': df.High,
        'low': df.Low,
        'type': 'candlestick',
        'name': acao,
        'showlegend': False
    }

    data = [tracel]
    layout = go.Layout()

    fig = go.Figure(data=data, layout=layout)
    return fig

#Criando sidebar

barra_lateral = st.sidebar.empty()

country_seleção = st.sidebar.selectbox("Selecione o país:", countries)
acoes = ip.get_stocks_list(country=country_seleção)
stock_seleção = st.sidebar.selectbox("Selecione o ativo:", acoes)

from_date = st.sidebar.date_input("De:", start_date)
to_date = st.sidebar.date_input("De:", end_date)

interval_seleção = st.sidebar.selectbox('Selecione o intervalo:', interval)

#Elementos centrais da Pág
st.title('Stock Monitor')
st.header('Ações')

st.subheader("Visualização gráfica")

grafico_candle = st.empty()
grafico_linha = st.empty()

df = consultar_acao(stock_seleção, country_seleção, format_date(from_date), format_date(to_date), interval_seleção)
fig = plotCandleStick(df)
grafico_candle = st.plotly_chart(fig)
grafico_linha = st.line_chart(df.Close)



