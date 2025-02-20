import pandas as pd
from web_data_extraction import get_latest_listings, gainers_losers, trending_latest, new_listings

def transform_latest_listings(json_data):
    # the normalise function flattens the nested JSON structure
    flattened_df = pd.json_normalize(json_data["data"])

    filtered_df = flattened_df[[
        'quote.USD.last_updated',
        'id', 
        'symbol', 
        'name', 
        'quote.USD.price', 
        'quote.USD.market_cap',
        'quote.USD.volume_24h',
        'quote.USD.price_change_24h',
        'quote.USD.percent_change_24h',
        'total_supply',
        'quote.USD.high_24h',
        'quote.USD.low_24h',
        'quote.USD.ath_price',
        'quote.USD.ath_date',
        'quote.USD.atl_price',
        'quote.USD.atl_date',
        'circulating_supply',
        'quote.USD.fully_diluted_market_cap'
    ]]

    cleaned_df = filtered_df.rename(columns={
        'quote.USD.last_updated': 'timestamp',
        'id': 'crypto_id',
        'quote.USD.price': 'price_usd',
        'quote.USD.market_cap': 'market_cap',
        'quote.USD.volume_24h': '24h_volume',
        'quote.USD.price_change_24h': 'price_change_24h',
        'quote.USD.percent_change_24h':             'price_change_percentage_24h',
        'quote.USD.high_24h': 'high_24h',
        'quote.USD.low_24h': 'low_24h',
        'quote.USD.ath_price': 'ath_price',
        'quote.USD.ath_date': 'ath_date',
        'quote.USD.atl_price': 'atl_price',
        'quote.USD.atl_date': 'atl_date',
        'quote.USD.fully_diluted_market_cap':   'fully_diluted_valuation'
    })

    return cleaned_df


def transform_gainers_losers(json_data):
    # flatten the nested JSON structure so each data point is easily accessible to be transformed into a python dataframe
    flattened_df = pd.json_normalize(json_data["data"])

    filter_columns = [
        "quote.USD.last_updated",
        "id",
        "symbol",
        "name",
        "quote.USD.price",
        "quote.USD.market_cap",
        "quote.USD.volume_24h",
        "quote.USD.percent_change_24h",
        "total_supply",
        "circulating_supply"
    ]

    filtered_df = flattened_df[filter_columns]

    # rename the previously embedded columns
    renaming_mapping = {
        "quote.USD.last_updated": "timestamp",
        "id": "crypto_id",
        "quote.USD.price": "price_usd",
        "quote.USD.market_cap": "market_cap",
        "quote.USD.volume_24h": "24h_volume",
        "quote.USD.percent_change_24h": "price_change_percentage_24h"
    }

    filtered_df = filtered_df.rename(columns=rename_map)

    return filtered_df


def transform_trending_latest(json_data):
    flattened_df = pd.json_normalize(json_data["data"])

    filter_columns = [
        "quote.USD.last_updated",
        "id",
        "symbol",
        "name",
        "quote.USD.price",
        "quote.USD.market_cap",
        "quote.USD.volume_24h",
        "quote.USD.percent_change_24h",
        "circulating_supply"
    ]

    df = flattened_df[filter_columns]

    renaming_mapping = {
        "quote.USD.last_updated": "timestamp",
        "id": "crypto_id",
        "quote.USD.price": "price_usd",
        "quote.USD.market_cap": "market_cap",
        "quote.USD.volume_24h": "24h_volume",
        "quote.USD.percent_change_24h": "price_change_percentage_24h"
    }

    flatten_df = flatten_df.rename(columns=renaming_mapping)

    return flatten_df

def new_listings(json_data):
    flattened_df = pd.json_normalize(json_data["data"])

    filter_columns = [
        "quote.USD.last_updated",
        "id",
        "symbol",
        "name",
        "quote.USD.price",
        "quote.USD.market_cap",
        "quote.USD.volume_24h",
        "quote.USD.percent_change_24h",
        "circulating_supply"
    ]

    df = flattened_df[filter_columns]

    renaming_mapping = {
        "quote.USD.last_updated": "timestamp",
        "id": "crypto_id",
        "quote.USD.price": "price_usd",
        "quote.USD.market_cap": "market_cap",
        "quote.USD.volume_24h": "24h_volume",
        "quote.USD.percent_change_24h": "price_change_percentage_24h"
    }

    flatten_df = flatten_df.rename(columns=renaming_mapping)

    return flatten_df