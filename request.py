"""
Connects to the coinmarketcap api to gather information about coins.

"""
import urllib3
import json
import pickle
import certifi
import os
from settings.settings import Settings

# TODO: save coin information in sqlite3
# TODO: read JSON data, determine how long to hold data in a pickle file (and how to delete)


class Scraper:
    """ A web scraper that connects to the CoinMarketCap API.

    Args:
        coins (List(Obj)): A list of coin.Coin objects.
    Attributes:
        coins (List(Obj)): A list of coin.Coin objects.
        time (int): The time the scrape retrived the data. (not implemented)
        link (str): The coinmarketcap api link.
        http (obj): A urllib3 object.
        settings (:obj: Settings): A Settings object that contains the settings.
    """

    def __init__(self, coins):
        self.coins = coins
        self.time = 0
        self.link = "https://api.coinmarketcap.com/v1/ticker/"
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                        ca_certs=certifi.where())
        self.settings = Settings()

    # TODO: replace ValueError with a logger.
    def get_coin_with_id(self, id):
        """
        Args:
            id (string): An id of a coin.Coin object.
        Return:
            returns coin.Coin with id id, if it exists.
        >>> import coin
        >>> btc = coin.Coin("bitcoin", "BTC", 8000, 10000, 10, -15)
        >>> b = Scraper([btc])
        >>> passes = b.get_coin_with_id("bitcoin")
        >>> passes.symbol
        'BTC'
        >>> fails = b.get_coin_with_id("fail")
        Traceback (most recent call last):
        ...
        ValueError: You have not added this coin in coins.txt!

        """
        for coin in self.coins:
            if coin.has_id(id):
                return coin
        raise ValueError("You have not added this coin in settings/coins.txt!")

    def update_frequency(self):
        """
        Returns:
            The number of minutes between the script updating the information.

        """
        return self.settings.update

    def print_coins(self):
        """
        Returns:
            A string of the coins this scraper searches for.

        >>> import  coin
        >>> lst = [coin.Coin("bitcoin", "BTC", 8000, 10000, 10, -10), \
        coin.Coin("litecoin", "LTC", 200, 400, 15, -15), \
        coin.Coin("monero", "XMR", 300, 500, 10, -5)]
        >>> test = Scraper(lst)
        >>> test.print_coins()
        Coins and Tokens:
        bitcoin
        litecoin
        monero

        """
        coins = self.coins
        result = "Coins and Tokens:"
        for coin in coins:
            result += "\n" + coin.id
        print(result)

    # TODO: work on exceptions
    def request_coin(self, name):
        """
        Requests data about a coin, stores data in this coin's pickle file.

        Args:
            name (str): a string that represents a Coin objects id.

        Returns:
            JSON data describing the coin with the id name.
        """
        try:
            r = self.http.request('GET', self.link + "/" + name)
            result = json.loads(r.data.decode('utf-8'))
            if result == {'error': 'id not found'}:
                raise ValueError("{} is either not a valid id or is not listed "
                                 "on CoinMarketCap.com. Please remove it from "
                                 "coins.txt".format(name))
            else:
                loc = 'Currencies/' + name
                try:
                    previous = self.__load(loc)
                    updated = previous + result
                    self.__dump(updated, loc)
                except FileNotFoundError:
                    self.__dump(result, loc)
                return result

        # error connecting to site
        except urllib3.exceptions.MaxRetryError:
            os.system(
                """osascript -e 'display notification "FAILED TO CONNECT" 
                with title "FATAL ERROR"'""")
            raise Exception("Failed to connect to server. Check internet "
                            "connection.")

        except ValueError:
            raise Exception("Something went wrong")

    def __load(self, file):
        """
        Load a pickled file.

        Args:
            file (file): A pickled file that contains information.

        Return:
            A string of data retrived from the pickle file `file`.

        """
        try:
            with open(file + ".pickle", 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("The file doesn't exist!")

    def __dump(self, obj, file):
        """
        Serialize the data gathered to access it elsewhere.

        Args:
            obj (:obj:): The object(s) to be serialized.

            file (file): The file the data will be stored in

        """
        with open(file + ".pickle", 'wb') as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    with open("coinList.pickle", "rb") as f:
        coins = pickle.load(f)
    test = Scraper(coins)
    for coin in coins:
        print(test.request_coin(coin.id))
