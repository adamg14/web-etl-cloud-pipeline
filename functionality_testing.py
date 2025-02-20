# convert these tests into builtin python unittests
from transform_data import transform_lastest_listings

json_response = {
    "data": [
        {
            "id": 1,
            "name": "Bitcoin",
            "symbol": "BTC",
            "slug": "bitcoin",
            "cmc_rank": 5,
            "num_market_pairs": 500,
            "circulating_supply": 16950100,
            "total_supply": 16950100,
            "max_supply": 21000000,
            "infinite_supply": False,
            "last_updated": "2018-06-02T22:51:28.209Z",
            "date_added": "2013-04-28T00:00:00.000Z",
            "tags": ["mineable"],
            "platform": None,
            "self_reported_circulating_supply": None,
            "self_reported_market_cap": None,
            "quote": {
                "USD": {
                    "price": 9283.92,
                    "volume_24h": 7155680000,
                    "price_change_24h": -150.0,
                    "percent_change_1h": -0.152774,
                    "percent_change_24h": 0.518894,
                    "percent_change_7d": 0.986573,
                    "market_cap": 852164659250.2758,
                    "fully_diluted_market_cap": 952835089431.14,
                    "high_24h": 9400.00,
                    "low_24h": 9200.00,
                    "ath_price": 19665.0,
                    "ath_date": "2017-12-16T00:00:00.000Z",
                    "atl_price": 65.53,
                    "atl_date": "2013-07-06T00:00:00.000Z",
                    "last_updated": "2018-08-09T22:53:32.000Z"
                }
            }
        },
        {
            "id": 1027,
            "name": "Ethereum",
            "symbol": "ETH",
            "slug": "ethereum",
            "num_market_pairs": 6360,
            "circulating_supply": 16950100,
            "total_supply": 16950100,
            "max_supply": 21000000,
            "infinite_supply": False,
            "last_updated": "2018-06-02T22:51:28.209Z",
            "date_added": "2013-04-28T00:00:00.000Z",
            "tags": ["mineable"],
            "platform": None,
            "quote": {
                "USD": {
                    "price": 1283.92,
                    "volume_24h": 7155680000,
                    "price_change_24h": -25.0,
                    "percent_change_1h": -0.152774,
                    "percent_change_24h": 0.518894,
                    "percent_change_7d": 0.986573,
                    "market_cap": 158055024432,
                    "fully_diluted_market_cap": 952835089431.14,
                    "high_24h": 1300.00,
                    "low_24h": 1250.00,
                    "ath_price": 1436.0,
                    "ath_date": "2018-01-13T00:00:00.000Z",
                    "atl_price": 0.43,
                    "atl_date": "2015-10-20T00:00:00.000Z",
                    "last_updated": "2018-08-09T22:53:32.000Z"
                }
            }
        }
    ]
}

# transform_latest_listings is working correctly
cleaned_df = transform_latest_listings(json_response)
print(cleaned_df.head())