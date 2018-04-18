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
        volume_alert (float): the % change in volume in a set time period that
            results in an alert.
        price_alert (float): The % change in price in a set time period that
            results in an alert.
        hour_change (float): The % change in the price of this Coin in the last
            hour of trading.
        day_change (float): The % change in the price of this Coin in the last
            24 hours of trading.
        to_btc (float): The price of this asset in terms of bitcoin.
        price (float): The price of this asset in terms of the chosen fiat
            currency.
        fiat (str): The fiat currency chosen in the settings file.

    """

    def __init__(self, id, symbol, vol_alert, price_alert):
        """
        Creates a new Coin object.

        Args:
            id (str): The id of this Coin.
            symbol(str) : The symbol of this Coin.
            vol_alert (float): The % change in volume in a set time period that
                results in an alert.
            price_alert (float): The % change in price in a set time period that
                results in an alert.
        """
        self.id = id
        self.symbol = symbol
        self.volume_alert = vol_alert
        self.price_alert = price_alert
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
            # if ret[1] == "hourly":
            #     self.time_frame = 0
            # elif ret[1] == "daily":
            #     self.time_frame = 1
            # elif ret[1] == "weekly":
            #     self.time_frame = 2
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
        self.volume_alert = value

    def get_vol(self):
        """

        :return:
        :rtype:
        """
        return self.volume_alert

    def set_price_alert(self, value):
        """

        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.price_alert = value

    def get_price_alert(self):
        """

        :return:
        :rtype:
        """
        return self.price_alert

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
                   self.volume_alert == other.volume_alert and \
                   self.price_alert == other.price_alert

    def price_notification(self):
        """
        Return True if a notification must be sent.
        :return:
        :rtype:
        """
        if self.change != 0:
            # price_alert if above positive threshold
            if self.change > 0 and self.price_alert > 0:
                if self.price_alert <= self.change:
                    return 1
            # price_alert if below negative threshold
            elif self.change < 0 and self.price_alert*-1 < 0:
                if -1 * self.price_alert >= self.change:
                    return -1
        return 0
