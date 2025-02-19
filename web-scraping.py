import requests
import pandas as pd

coinmarketcap_api = "28837f41-1f64-4b04-8bc0-2ac2fc9ac559"

def get_latest_listings():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": coinmarketcap_api,
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def gainers_losers():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/gainers-losers"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": coinmarketcap_api,
    }
    parameters = {
        "start": "1",    
        "limit": "10",   
        "convert": "USD" 
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    return data


def trending_latest():
    # based off traffic to coin detail pages
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/most-visited"
    header = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": coinmarketcap_api,
    }
    parameters  = {
        "start": "1",    
        "limit": "10",   
        "convert": "USD"
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    return data


def new_listings():
    url = 
    header = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": coinmarketcap_api,
    }
    parameters  = {
        "start": "1",    
        "limit": "10",   
        "convert": "USD"
    }

    response = requests.get(url, headers=headers, params=params)

    return data
# get social media activity for each of the cryptos for the day - to have a word cloud type figure
