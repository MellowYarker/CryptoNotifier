"""
A class that represents a cryptocurrency asset.

"""

# TODO: use properties if needed, getters/setters aren't pythonic.
from currency_converter import CurrencyConverter
from settings.settings import Settings


class Coin:
    """
    A cryptocurrency asset.

    Attributes:
        id (str): The id of the Coin. Ex: bitcoin, ethereum.
        symbol (str): The symbol of the Coin. Ex: BTC, ETH.
        buy_price (float): The price at which a Coin is worth buying.
        sell_price (float): The desired price at which to sell a Coin.
        increase_alert (float): The % increase in price in a set time
            period that results in a change_alert.
        decrease_alert (float): The % decrease in price in a set time
            period that results in a change_alert.
        change (float): The percent change in price over the desired duration
            in the settings file.
        to_btc (float): The price of this asset in terms of bitcoin.
        price (float): The price of this asset in terms of the chosen fiat
            currency.
    """

    def __init__(self, id, symbol, buy_alert, sell_alert, increase_alert,
                 decrease_alert):
        """
        Creates a new Coin object.

        Args:
            id (str): The id of this Coin.
            symbol(str): The symbol of this Coin.
            buy_alert (float): The price at which a Coin is worth buying.
            sell_alert (float): The desired price at which to sell a Coin.
            increase_change_alert (float): The % increase in price in a set time
                period that results in a change_alert.
            decrease_change_alert (float): The % decrease in price in a set time
                period that results in a change_alert.
        """
        self.id = id
        self.symbol = symbol

        self.buy_price = buy_alert
        self.sell_price = sell_alert

        self.increase_alert = increase_alert
        self.decrease_alert = decrease_alert

        self.change = 0
        self.to_btc = 0
        self.price = 0

    def set_btc_value(self, value):
        """
        Sets the bitcoin value of this Coin to value.

        Args:
            value: A float that represents the bitcoin value of this Coin.

        Returns:
            None
        """
        self.to_btc = value

    def set_price(self, value):
        """
        Sets the price of this Coin. If it can't be converted to the desired
        currency (from the settings) it defaults to USD.

        Args:
            value (float): The value of this Coin in USD. This is a direct
                result from the coinmarketcap API

        """
        c = CurrencyConverter()
        try:
            self.price = c.convert(value, 'USD', Settings().fiat)
        except ValueError:
            self.price = value
            # TODO ADD A LOGGER HERE THAT SAYS IT COULDN'T CONVERT TO THE
            # SETTINGS CURRENCY

    def has_id(self, id):
        """
        Determine if this id belongs to this Coin

        args:
            id (string): A string that might be a coin id.

        Returns:
            True if this Coin has id id.

        """
        return self.id == id

    # TODO: See usage and determine if this is detailed enough *might need price
    def __eq__(self, other):
        """
        Compare two Coin objects.

        args:
            other (:object:): A Coin object.

        Returns:
            True if other is equivalent to this Coin.

        """
        if type(self) == type(other):
            return self.id == other.id and self.symbol == other.symbol and \
                   self.buy_price == other.buy_price and \
                   self.sell_price == other.sell_price and \
                   self.increase_alert == other.increase_alert and \
                   self.decrease_alert == other.decrease_alert

    def change_notification(self):
        """
        Determins whether an increase, decrease, or no alert should
        be made.

        Returns:
            1 if a price increased at least the increase_alert amount
            -1 if a price decreased at least the decrease_alert amount
            0 otherwise.

        """
        if self.change != 0:
            # price_change_alert if above positive threshold
            if self.change > 0:
                if abs(self.increase_alert) <= self.change:
                    return 1
            # price_change_alert if below negative threshold
            elif self.change < 0:
                if -1 * abs(self.decrease_alert) >= self.change:
                    return -1
        return 0

    def buy_notification(self):
        """
        Determine if a buy alert should be triggered. Takes priority over price
        change.

        Returns:
            True if a buy alert should be triggered; False otherwise
        """
        return self.buy_price >= self.price

    def sell_notification(self):
        """
        Determine if a sell alert should be triggered. Takes priority over price
        change.

        Returns:
            True if a sell alert should be triggered; False otherwise.
        """
        return self.sell_price <= self.price
