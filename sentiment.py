import pandas as pd
import numpy as np
import requests
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import seaborn as sns

load_dotenv()
API_KEY = os.getenv('ALPHAVANTAGE_APIKEY')  # Replace with your own API Key

# Implement statistical tests to determine whether the mean or median is a more accurate representation of the 'average'
# X <= -0.35: Bearish, -0.35 < x <= -0.15: Somewhat Bearish, -0.15 < x < 0.15: Neutral; reflect
def sentiment_extractor(ticker):
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()

    scores = [item['overall_sentiment_score'] for item in data['feed']]

    df = pd.DataFrame({'score': scores})
    print(f"Mean: {df['score'].mean():.3f}")
    print(f"Median: {df['score'].median():.3f}")
    print(f"Skewness: {df['score'].skew():.3f}")

    sns.histplot(df['score'], kde=True, bins=20)
    plt.axvline(df['score'].mean(), color='red', ls='--', label='Mean')
    plt.axvline(df['score'].median(), color='green', ls='--', label='Median')
    plt.show()

sentiment_extractor('AAPL')