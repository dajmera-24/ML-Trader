import pandas as pd
import numpy as np
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ALPHAVANTAGE_APIKEY')  # Replace with your own API Key

def sentiment_extractor(ticker):
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()

    # print(data)