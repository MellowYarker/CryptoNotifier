"""
Parses settings/coins.txt

"""
from coin import Coin
import pickle


def rebuild():
    """
    Returns:
        True if either settings/coins.txt has been modified or coinList.pickle
            doesn't exist.
        False otherwise.

    """
    # build a list of Coin objects from the coins.txt file
    coins = create_coins("settings/coins.txt")

    try:
        with open("coinList.pickle", "rb") as p:
            p = pickle.load(p)
        return coins != p
    except FileNotFoundError:
        return True


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


def run():
    """
    Run this file. If coins.txt or settings.txt have been modified the new
    Coin objects will be used, otherwise, previous Coin objects will be updated.

    """
    if rebuild():
        coins = create_coins("settings/coins.txt")

        with open('coinList.pickle', 'wb') as file:
            pickle.dump(coins, file)


if __name__ == "__main__":
    run()
