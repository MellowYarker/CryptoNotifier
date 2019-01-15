from math import ceil

"""
    FIAT (str): The fiat currency chosen in the settings file.
    TIME_FRAME (str): The time frame to analyze this Coin object over.
    UPDATE (int): The number of seconds between data requests.
"""
# TODO: if settings already exist, is it faster to compare them
#       or just update them no matter what.

def set_settings():
    """
        Parse settings.txt and return the important values.
    """
    try:
        with open("settings/settings.txt", 'r') as f:
            settings = f.read()
            settings = settings.split('\n')

        FIAT = str(settings[0])
        if settings[1] == "hourly" or settings[1] == "daily" or settings[1] == "weekly":
            TIME_FRAME = settings[1]
        else:
            raise ValueError("settings/settings.txt line 2 must be one of "
                                + "(hourly, daily, weekly)! Default: daily"
                                + "price change.")
        # must be an integer
        UPDATE = ceil(int(settings[2])) * 60

    except ValueError:
        # defaults to USD
        FIAT = "USD"
        # defaults to 24 hour changes
        TIME_FRAME = "daily"
        # defaults to 30 minutes
        UPDATE = 30 * 60

    return FIAT, TIME_FRAME, UPDATE

FIAT, TIME_FRAME, UPDATE = set_settings()
