import pandas as pd
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
api_key = "O9EVJ9EHW8ZACHJE"
ticker = "CRYPTO:BTC"

url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&topics=blockchain&apikey={api_key}"
r = requests.get(url)

data = r.json()

print(data["feed"][0])


df = pd.json_normalize(data["feed"])
