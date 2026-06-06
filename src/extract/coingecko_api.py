import pandas as pd 
import requests  
import numpy as np  
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_COINGECKO_KEY")

IS_PRO_PLAN = False 
if IS_PRO_PLAN:
    base_url = "https://pro-api.coingecko.com/api/v3"
    headers = {"x-cg-pro-api-key": API_KEY, "accept": "application/json"}
else:
    base_url = "https://api.coingecko.com/api/v3"
    headers = {"x-cg-demo-api-key": API_KEY, "accept": "application/json"}

#Function crawl data from CoinGecko
def get_top_coins(per_page=250):

    endpoint = f"{base_url}/coins/markets"
    params = {
        "vs_currency": "usd",      
        "order": "market_cap_desc",
        "per_page": per_page,           
        "page": 1
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    return pd.DataFrame(data)