"""
Parses settings/coins.txt

"""
from coin import Coin
import pickle

def run():
    """
    If coins.txt or settings.txt have been modified, the new Coin objects will be used.
    Otherwise, the previous Coin objects will be updated.

    Returns:
        None

    """
    # TODO: read+write without opening file more than once.
    # build a list of Coin objects from the coins.txt file
    coins = create_coins("settings/coins.txt")

    try:
	# coinList.pickle is where the serialized coins are.
        with open("coinList.pickle", "rb") as p:
            p = pickle.load(p)

	# Coin objects have their own equivalence operator.
	# See coin.py for implementation.
        if coins != p:
            with open('coinList.pickle', 'wb') as file:
                pickle.dump(coins, file)

    except FileNotFoundError:
        with open('coinList.pickle', 'wb') as file:
            pickle.dump(coins, file)


def create_coins(file):
    """
    Return:
        a list of Coin objects created from file file.

    """
    with open(file, 'r') as f:
        strings = f.readlines()
        coins = []
        for coin in strings:
            coin = coin.split(", ")
            try:
                coins.append(
                    Coin(coin[0],
                         coin[1],
                         float(coin[2]),
                         float(coin[3]),
                         float(coin[4]),
                         float(coin[5][:-1])))
            except ValueError:
                raise ValueError("Please check settings/coins.txt to make sure"
                                 " the document is formatted correctly.")
    return coins


if __name__ == "__main__":
    run()
