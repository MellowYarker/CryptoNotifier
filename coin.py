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
        id (str): The id of the Coin. Ex bitcoin, ethereum.
        symbol (str): The symbol of the Coin. Ex: BTC, ETH.
        buy_price (float): The price at which a Coin is worth buying.
        price_alert (float): The % change in price in a set time period that
            results in an price_alert.
        to_btc (float): The price of this asset in terms of bitcoin.
        price (float): The price of this asset in terms of the chosen fiat
            currency.
    """

    def __init__(self, id, symbol, buy_alert, price_alert):
        """
        Creates a new Coin object.

        Args:
            id (str): The id of this Coin.
            symbol(str): The symbol of this Coin.
            buy_alert (float): The price at which a Coin is worth buying.
            price_alert (float): The % change in price in a set time period that
                results in an price_alert.
        """
        self.id = id
        self.symbol = symbol
        self.buy_price = buy_alert
        self.price_change_alert = price_alert
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

        :param value:
        :type value:
        :return:
        :rtype:
        """
        c = CurrencyConverter()
        try:
            self.price = c.convert(value, 'USD', Settings().fiat)
        except ValueError:
            self.price = value
            # TODO ADD A LOGGER HERE THAT SAYS IT COULDN'T CONVERT
            # TO THE SETTINGS CURRENCY

    def has_id(self, id):
        """
        Return True if this Coin has id id.


        """
        return self.id == id

    # TODO: See usage and determine if this is detailed enough *might need price
    def __eq__(self, other):
        """
        Return True if this Coin is equivalent to other.

        """
        if type(self) == type(other):
            return self.id == other.id and self.symbol == other.symbol and \
                   self.buy_price == other.buy_price and \
                   self.price_change_alert == other.price_change_alert

    # TODO: refactor this method once individual increase/decrease options exist
    def price_notification(self):
        """
        Determins whether an increase, decrease, or no price price_alert should
        be made.

        Returns:
            1 if a price increased at least the price_alert amount
            -1 if a price decreased at least the price_alert amount
            0 otherwise.

        """
        if self.change != 0:
            # price_change_alert if above positive threshold
            if self.change > 0 and self.price_change_alert > 0:
                if self.price_change_alert <= self.change:
                    return 1
            # price_change_alert if below negative threshold
            elif self.change < 0 and self.price_change_alert*-1 < 0:
                if -1 * self.price_change_alert >= self.change:
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
        pass
