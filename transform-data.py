from web-scraping import get_latest_listings,
gainers_loser,
trending_latest
new_listings
import pandas as pd


def transform_data(json_data):
    # the normalise function flattens the nested JSON structure
    flattened_df = pd.json_normalize(json_response["data"])

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