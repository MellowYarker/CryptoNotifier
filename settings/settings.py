"""
This is the settings class.

Other classes can access this class to determine data like the desired time
frame.

"""
from math import ceil


class Settings:
    """

    Attributes:
        time_frame (str): The time frame to analyze this Coin object over.
        fiat (str): The fiat currency chosen in the settings file.
        update (int): The number of seconds between data requests.

    """

    def __init__(self):
        try:
            with open("settings/settings.txt", 'r') as f:
                ret = f.read()
                ret = ret.split('\n')

            self.fiat = str(ret[0])
            if ret[1] == "hourly" or ret[1] == "daily" or ret[1] == "weekly":
                self.time_frame = ret[1]
            else:
                raise ValueError("settings/settings.txt line 2 must be one of "
                                 + "(hourly, daily, weekly)! Default: daily"
                                 + "price change.")
            # must be an integer
            self.update = ceil(int(ret[2])) * 60
        except ValueError:
            # defaults to USD
            self.fiat = "USD"
            # defaults to 24 hour changes
            self.time_frame = "daily"
            # defaults to 30 minutes
            self.update = 30 * 60