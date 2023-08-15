import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def impute_max_supply(df):
    for crypto_id, max_supply in max_supply_values.items():
        mask = (df['Cryptocurrency'] == crypto_id) & df['Max_Supply'].isnull()
        df.loc[mask, 'Max_Supply'] = max_supply
    return df

# Lista de criptomonedas y sus respectivos Max_Supply
max_supply_values = {
    'solana': 500000000.0,
    'uniswap': 1000000000.0,
    'decentraland': 2805886393.0,
    'chiliz': 8888888888.0,
    'axie-infinity': 270000000.0,
    'the-sandbox': 300000000.0,
    'cardano': 45000000000.0,
    'quant-network': 14612493.0,
    'chainlink': 1000000000.0,
    'iota': 2779530283.0
}

def fill_description_nans(df):
    df['Description'].fillna(method='ffill', inplace=True)
    return df


def process_cryptocurrency_data(df, cryptocurrency_name):
    # Filtrar los datos para la criptomoneda especificada
    crypto_data = df[df['Cryptocurrency'] == cryptocurrency_name]

    if crypto_data.empty:
        print(f"No se encontraron datos para la criptomoneda '{cryptocurrency_name}'.")
        return None

    # Convertir 'timestamp' en datetime y establecerlo como índice
    crypto_data['timestamp'] = pd.to_datetime(crypto_data['timestamp'])
    crypto_data.set_index('timestamp', inplace=True)

    return crypto_data


def generate_crypto_analysis_plots(df, cryptocurrency_name):
    sns.set_context("talk")

    # Usar la función para procesar los datos de la criptomoneda
    crypto_data = process_cryptocurrency_data(df, cryptocurrency_name)
    if crypto_data is None:
        return

    # Gráfico de Evolución del Precio de la Criptomoneda a lo Largo del Tiempo
    plt.figure(figsize=(10, 6))
    plt.plot(crypto_data['Price'])
    plt.title(f'Evolución del Precio de {cryptocurrency_name.capitalize()} a lo Largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Gráfico de Capitalización de Mercado por Año
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Year', y='Market_Cap_Rank', data=crypto_data)
    plt.title(f'Capitalización de Mercado de {cryptocurrency_name.capitalize()} por Año')
    plt.xlabel('Año')
    plt.ylabel('Capitalización de Mercado')
    plt.ylim(0, 20)
    plt.show()

    # Gráfico de Relación entre Precio y Volumen Total
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Price', y='Total_Volume', data=crypto_data)
    plt.title(f'Relación entre Precio y Volumen Total de {cryptocurrency_name.capitalize()}')
    plt.xlabel(f'Precio de {cryptocurrency_name.capitalize()}')
    plt.ylabel(f'Volumen Total de {cryptocurrency_name.capitalize()}')
    plt.show()

    # Gráfico de Distribución de Precios por Año
    sns.set_style("whitegrid")
    sns.set_palette("pastel")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Year', y='Price', data=crypto_data)
    plt.title(f'Distribución de Precios de {cryptocurrency_name.capitalize()} por Año', fontsize=16, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Precio', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()