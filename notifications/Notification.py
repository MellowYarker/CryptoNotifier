"""
The notification class.
"""
import os


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

    def action(self, change):
        """
        Returns:
            - a string based on the movement of an asset.
        """
        if change > 0:
            return "risen"
        else:
            return "fallen"


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
        if self.asset.time_frame == "hourly":
            self.message = self.build_message("{id} ({symbol}) has "
                                              "{change} by {amount}% "
                                              "in the last hour! Current "
                                              "price is {price} {fiat}")
        elif self.asset.time_frame == "daily":
            self.message = self.build_message("{id} ({symbol}) has {change} "
                                              "by {amount}% in the last 24 "
                                              "hours! Current price is "
                                              "{price} {fiat}")

        elif self.asset.time_frame == "weekly":
            self.message = self.build_message(
                "{id} ({symbol}) has {change} by {amount}% in the last week! " +
                "Current price is {price} {fiat}")

    def build_message(self, msg):
        """
        Helps with message construction.

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
                          fiat=str(self.asset.fiat))

    def notify(self):
        """
        Displays the notification.

        """
        os.system(
            """osascript -e 'display notification "{}" with title "{}"'""".\
            format(self.message, self.title))


class VolumeNotification(Notification):
    """
    A notification representing a change in volume.

    """

    def __init__(self, asset, change):
        """
        Create a new VolumeNotification

        """
        pass
