"""
Parses the json and assigns data to Coin objects.
"""

from settings.settings import Settings

# TODO: does this need to be in its own file?


def parse(coin, data):
    """
    Parse the JSON data and assign relevant information to the coin object.

    Args:
        coin (:obj: coin.Coin): A coin object.
        data (:obj: json): JSON data retrieved from coinmarketcap about a coin.

    Returns:
        None

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
