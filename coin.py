"""
A class that represents a cryptocurrency asset.

"""

# TODO: use properties if needed, getters/setters aren't pythonic.
from currency_converter import CurrencyConverter
from math import ceil


class Coin:
    """
    A cryptocurrency asset.

    Attributes:
        id (str): The id of the Coin. Ex bitcoin, ethereum.
        symbol (str): The symbol of the Coin. Ex: BTC, ETH.
        buy_price (float): The price at which a Coin is worth buying.
        price_alert (float): The % change in price in a set time period that
            results in an price_alert.
        hour_change (float): The % change in the price of this Coin in the last
            hour of trading.
        day_change (float): The % change in the price of this Coin in the last
            24 hours of trading.
        to_btc (float): The price of this asset in terms of bitcoin.
        price (float): The price of this asset in terms of the chosen fiat
            currency.
        fiat (str): The fiat currency chosen in the settings file.

    """

    def __init__(self, id, symbol, buy_alert, price_alert):
        """
        Creates a new Coin object.

        Args:
            id (str): The id of this Coin.
            symbol(str) : The symbol of this Coin.
            buy_alert (float): The price at which a Coin is worth buying.
            price_alert (float): The % change in price in a set time period that
                results in an price_alert.
        """
        self.id = id
        self.symbol = symbol
        self.buy_price = buy_alert
        self.price_change_alert = price_alert
        self.time_frame = ""
        self.change = 0
        # TODO: hour and day and week change(s) will be irrelevant soon
        self.hour_change = 0
        self.day_change = 0
        self.week_change = 0
        self.to_btc = 0
        self.price = 0
        self.update = 30
        try:
            with open("settings.txt", 'r') as f:
                ret = f.read()
                ret = ret.split('\n')

            self.fiat = str(ret[0])
            if ret[1] == "hourly" or ret[1] == "daily" or ret[1] == "weekly":
                self.time_frame = ret[1]
            else:
                raise ValueError("settings.txt line 2 must be one of " +
                                 "(hourly, daily, weekly)! Defaulting to daily"
                                 + "price change.")
            # must be an integer
            self.update = ceil(int(ret[2])) * 60
        except ValueError:
            # defaults to USD
            self.fiat = "USD"
            # will default to 24 hour changes
            self.time_frame = "daily"
            # update frequency defaults to 30 minutes
            self.update = 30 * 60

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
            self.price = c.convert(value, 'USD', self.fiat)
        except ValueError:
            self.price = value
            # TODO ADD A LOGGER HERE THAT SAYS IT COULDN'T CONVERT
            # TO THE SETTINGS CURRENCY

    def get_price(self):
        """

        :return:
        :rtype:
        """
        return self.price

    def set_vol(self, value):
        """

        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.buy_price = value

    def get_buy_price(self):
        """

        :return:
        :rtype:
        """
        return self.buy_price

    def set_price_change_alert(self, value):
        """

        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.price_change_alert = value

    def get_price_change_alert(self):
        """

        :return:
        :rtype:
        """
        return self.price_change_alert

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
        Determins whether an increase, decrease, or no price price_alert should be
        made.

        Returns:
            1 if a price increased at least the price_alert amount
            -1 if a price decreaed at least the price_alert amount
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

    def buy_notifiaction(self):
        """
        Determine if a buy alert should be triggered. Takes priority over price
        change.

        Returns:
            True if a buy  should be triggered and False otherwise
        """
        return self.buy_price >= self.price

    def sell_notification(self):
        """
        Determine if a sell alert should be triggered. Takes priority over price
        change.

        Returns:
            True if a sell alert should be triggered and False otherwise.
        """
        pass
