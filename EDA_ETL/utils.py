import streamlit as st
import pandas as pd
import altair as alt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('Datasets/Data_ingested/crypto_data_general.csv')

# Filtrar los datos para la criptomoneda Solana
solana_data = df[df['Cryptocurrency'] == 'solana']

# Convertir la columna 'timestamp' en formato datetime
solana_data['timestamp'] = pd.to_datetime(solana_data['timestamp'])

# Configurar la página para ocupar toda la pantalla
st.set_page_config(layout="wide")

# Título
st.title('Cryptocurrency Price Analysis')

# Gráfico de evolución del precio de Solana
chart = alt.Chart(solana_data).mark_line().encode(
    x='timestamp:T',
    y='Price:Q',
    tooltip=['timestamp:T', 'Price:Q']
).properties(
    width=800,
    height=400
).interactive()

st.altair_chart(chart)
