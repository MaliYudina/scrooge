import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'YOUR_API_KEY'


from log_work.log_setup import setup_logger
logger = setup_logger()
logger.info('call_moex_api_coupons start')
LOGGER = logger


def get_history_prices(secid):
    """

    """
    LOGGER.info("1. Start get_history_prices from Alpha_vantage API...", )

    # Create an Alpha Vantage client for time series data
    ts = TimeSeries(key=api_key, output_format='pandas')

    # Fetch daily historical data for AAPL
    data, meta_data = ts.get_daily(symbol=secid, outputsize='full')

    # Extract and plot the closing prices
    closing_prices = data['4. close']
    closing_prices = closing_prices.iloc[::-1]  # Reverse the order to have the oldest data first

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(closing_prices, label='Closing Prices', color='blue')
    plt.title('Historical Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

