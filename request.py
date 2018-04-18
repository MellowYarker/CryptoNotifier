"""
Connects to the coinmarketcap api to get info about coin prices

"""
import urllib3
import json
import pickle
import certifi

# TODO: save coin information in sqlite3
# TODO: read JSON data, determine how long to hold data in a pickle file (and how to delete)


class Bot:
    """ A bot that connects to the CoinMarketCap API.

    Args:
        coins (List(Obj)): A list of coin.Coin objects.
    Attributes:
        coins (List(Obj)): A list of coin.Coin objects.
        time (int): The time the bot retrived the data. (not implemented)
        link (str): The coinmarketcap api link.
        http (obj): A urllib3 object.
    """

    def __init__(self, coins):
        self.coins = coins
        self.time = 0
        self.link = "https://api.coinmarketcap.com/v1/ticker/"
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                        ca_certs=certifi.where())

    # TODO: replace ValueError with a logger.
    def get_coin_with_id(self, id):
        """
        Return:
            returns coin.Coin with id id, if it exists.

        >>> btc = coin.Coin("bitcoin", "BTC", 5, 10)
        >>> b = Bot([btc])
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
        raise ValueError("You have not added this coin in coins.txt!")

    def update_frequency(self):
        """
        Returns:
            - the number of minutes between the script updating the information.

        """
        return self.coins[0].update

    def print_coins(self):
        """
        Returns:
            a string of the _coins this bot searches for.

        """
        coins = self.coins
        result = ""
        for coin in coins:
            result += coin + "\n"

    # TODO: work on exceptions
    def request_coin(self, name):
        """
        Requests data about a coin, stores data in this coins pickle file.

        Args:
            name (str): a string that represents a Coin objects id.

        Returns
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

        except ValueError:
            raise Exception("Something went wrong")

    def __load(self, file):
        """
        Load a pickled file.

        Return:
            A string of data retrived from the pickle file file.

        """
        try:
            with open(file + ".pickle", 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("The file doesn't exist!")

    def __dump(self, obj, file):
        """
        Serialize the data gathered to access it elsewhere.

        """
        with open(file + ".pickle", 'wb') as f:
            pickle.dump(obj, f)


if __name__ == "__main__":
    with open("coinList.pickle", "rb") as f:
        coins = pickle.load(f)
    test = Bot(coins)
    for coin in coins:
        print(test.request_coin(coin.id))
