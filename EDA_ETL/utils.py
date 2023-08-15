import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def impute_max_supply(df):
     for crypto_id, max_supply in max_supply_values.items():
         mask = (df['Cryptocurrency'] == crypto_id) & df['Max_Supply'].isnull()
         df.loc[mask, 'Max_Supply'] = max_supply
     return df

# List of cryptocurrencies and their respective Max_Supply
max_supply_values = {
     'sunny': 500000000.0,
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
     # Filter the data for the specified cryptocurrency
     crypto_data = df[df['Cryptocurrency'] == cryptocurrency_name]

     if crypto_data.empty:
         print(f"No data found for cryptocurrency '{cryptocurrency_name}'.")
         return None

     # Convert 'timestamp' to datetime and set it as index
     crypto_data['timestamp'] = pd.to_datetime(crypto_data['timestamp'])
     crypto_data.set_index('timestamp', inplace=True)

     return crypto_data


def generate_crypto_analysis_plots(df, cryptocurrency_name):
     sns.set_context("talk")

     # Use the function to process the cryptocurrency data
     crypto_data = process_cryptocurrency_data(df, cryptocurrency_name)
     if crypto_data is None:
         return

     # Graph of Cryptocurrency Price Evolution over Time
     plt.figure(figsize=(10, 6))
     plt.plot(crypto_data['Price'])
     plt.title(f'Price Evolution of {cryptocurrency_name.capitalize()} over Time')
     plt.xlabel('Date')
     plt.ylabel('Price')
     plt.xticks(rotation=45)
     plt.tight_layout()
     plt.show()

     # Market Cap by Year Chart
     plt.figure(figsize=(12, 8))
     sns.barplot(x='Year', y='Market_Cap_Rank', data=crypto_data)
     plt.title(f'Market Capitalization of {cryptocurrency_name.capitalize()} per Year')
     plt.xlabel('Year')
     plt.ylabel('Market Capitalization')
     plt.ylim(0, 20)
     plt.show()

     # Graph of Relationship between Price and Total Volume
     plt.figure(figsize=(12, 8))
     sns.scatterplot(x='Price', y='Total_Volume', data=crypto_data)
     plt.title(f'Ratio between Price and Total Volume of {cryptocurrency_name.capitalize()}')
     plt.xlabel(f'Price of {cryptocurrency_name.capitalize()}')
     plt.ylabel(f'Total Volume of {cryptocurrency_name.capitalize()}')
     plt.show()

     # Price Distribution Graph per Year
     sns.set_style("whitegrid")
     sns.set_palette("pastel")
     plt.figure(figsize=(10, 6))
     sns.boxplot(x='Year', y='Price', data=crypto_data)
     plt.title(f'Price Distribution of {cryptocurrency_name.capitalize()} by Year', fontsize=16, fontweight='bold')
     plt.xlabel('Year', fontsize=12)
     plt.ylabel('Price', fontsize=12)
     plt.xticks(rotation=45)
     plt.tight_layout()
     plt.show()