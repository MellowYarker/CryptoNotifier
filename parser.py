"""
Parses the json and assigns data to Coin objects.
"""


def parse(coin, data):
    """
    I'll write this later basically it just parses the data from json and
    associates to coin objects.

    hour day and week remain for now in case I want to do something with them
    in the near future. This will be cleaner soon enough and I may move it
    to a class instead of having it alone in this file.

    """
    coin.set_price(float(data[0]['price_usd']))
    coin.set_btc_value(float(data[0]['price_btc']))
    coin.hour_change = float(data[0]['percent_change_1h'])
    coin.day_change = float(data[0]['percent_change_24h'])
    coin.week_change = float(data[0]['percent_change_7d'])
    if coin.time_frame == "hourly":
        coin.change = coin.hour_change
    elif coin.time_frame == "daily":
        coin.change = coin.day_change
    elif coin.time_frame == "weekly":
        coin.change = coin.week_change
