"""
The notification class.
"""
import os
from settings.settings import Settings


class Notification:
    """
    A notification class.

    Args:
        asset: (coin.Coin): A Coin object.

    Attributes:
        asset: (coin.Coin): A Coin object.
        title (str): This Notification's title.
        message (str): This Notification's message.
    """

    def __init__(self, asset):
        self.asset = asset
        self.title = "ALERT"
        self.message = ""
        self.settings = Settings()

    def notify(self):
        """
        Displays the notification.

        """
        os.system(
            """osascript -e 'display notification "{}" with title "{}"'""".
            format(self.message, self.title))


class PriceNotification(Notification):
    """
    A price notification is a type of notification that triggers when a
    cryptocurrency's (asset) price changes by a certain amount.

    Args:
        asset: (coin.Coin): A Coin object.
        change (int): an integer that represents whether the price of the asset
        increased or decreased.

    Attributes:
        asset (coin.Coin): A Coin object.
        title (str): This PriceNotification's title.
        message (str): This PriceNotification's message.
        change (int): an integer that represents whether the price of the asset
        increased or decreased.
    """
    def __init__(self, asset, change):
        Notification.__init__(self, asset)
        self.change = change

    def set_message(self):
        """
        Sets this PriceNotifications message to a custom message based on the
        price action of this asset.

        """
        if self.settings.time_frame == "hourly":
            self.message = self.help_build("{id} ({symbol}) has "
                                           "{change} by {amount}% "
                                           "in the last hour! Current "
                                           "price is {price} {fiat}")
        elif self.settings.time_frame == "daily":
            self.message = self.help_build("{id} ({symbol}) has {change} "
                                           "by {amount}% in the last 24 "
                                           "hours! Current price is "
                                           "{price} {fiat}")

        elif self.settings.time_frame == "weekly":
            self.message = self.help_build(
                "{id} ({symbol}) has {change} by {amount}% in the last week! " +
                "Current price is {price} {fiat}")

    def action(self, change):
        """
        Returns:
            - a string based on the movement of an asset.
        """
        if change > 0:
            return "risen"
        else:
            return "fallen"

    def help_build(self, msg):
        """
        Helps build the message.

        Args:
            msg (str): the message that needs to be formatted

        Returns:
            The properly formatted message as a string.

        """
        return msg.format(id=self.asset.id,
                          symbol=self.asset.symbol,
                          change=self.action(self.change),
                          amount=str(self.asset.change),
                          price=format(self.asset.price, '.2f'),
                          fiat=str(self.settings.fiat))


class TradeNotification(Notification):
    """
    A notification representing a buying or selling opportunity for an asset.

    Args:
        asset: (coin.Coin): A Coin object.

    Attributes:
        asset (coin.Coin): A Coin object.
        title (str): This TradeNotification's title.
        message (str): This TradeNotification's message.
    """
    def __init__(self, asset):
        """
        Creates a new TradeNotification

        """
        Notification.__init__(self, asset)

    def set_message(self):
        """
        Build the message for this TradeNotification based on if an asset should
        be bought or sold at the current price.

        Returns:
            None
        """

        if self.asset.buy_notification():
            self.message = self.help_build("BUY ALERT: {id} ({symbol}) is worth"
                                           " {price} {fiat}!")
        elif self.asset.sell_notification():
            self.message = self.help_build("SELL ALERT: {id} ({symbol}) is "
                                           "worth {price} {fiat}!")

    def help_build(self,  msg):
        """
        Helps build the message.

        Args:
            msg (str): the message that needs to be formatted

        Returns:
            The properly formatted message as a string.

        """
        return msg.format(id=self.asset.id,
                          symbol=self.asset.symbol,
                          price=self.asset.price,
                          fiat=self.settings.fiat)


class VolumeNotification(Notification):
    """
    A notification representing a change in volume.

    """

    def __init__(self, asset, change):
        """
        Create a new VolumeNotification

        """
        pass
