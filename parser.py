"""
Parses the json and assigns data to Coin objects.
"""

from settings.settings import Settings


def parse(coin, data):
    """
    I'll write this later basically it just parses the data from json and
    associates to coin objects.

    hour day and week remain for now in case I want to do something with them
    in the near future. This will be cleaner soon enough and I may move it
    to a class instead of having it alone in this file.

    """
    settings = Settings()
    coin.set_price(float(data[0]['price_usd']))
    coin.set_btc_value(float(data[0]['price_btc']))
    coin.change = assign(settings, data)


def assign(settings, data):
    """
    Returns the correct price percent change based on the time_frame in settings

    Args:
         settings (:obj: Settings): A Settings object.
         data (:obj: json): json data about a coin.
    Returns:
        requested price percent change as a float.
    """
    options = {"hourly": float(data[0]['percent_change_1h']),
               "daily": float(data[0]['percent_change_24h']),
               "weekly": float(data[0]['percent_change_7d'])}
    return options[settings.time_frame]
