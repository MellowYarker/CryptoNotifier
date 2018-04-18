"""
Parses coins.txt and settings.txt

"""
from coin import Coin
import pickle


def rebuild():
    """
    Returns:
        True if either the coins.txt or settings.txt file has been modified,
        False if neither has been modified.

    """
    # build a list of Coin objects from the coins.txt.txt file
    coins = create_coins("coins.txt")

    try:
        with open("coinList.pickle", "rb") as p:
            p = pickle.load(p)
        with open("settings.txt", "r") as s:
            s = s.read().split("\n")
        return coins != p or p[0].fiat != s[0] or p[1].time_frame != s[1]\
            or p[2].update // 60 != int(s[2])
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
                    Coin(coin[0], coin[1], float(coin[2]), float(coin[3][:-1])))
            except ValueError:
                raise ValueError("Please check coins.txt to make sure the " +
                                 "document is formatted correctly.")
    return coins


def run():
    """
    Run this file. If coins.txt or settings.txt have been modified the new
    Coin objects will be used, otherwise, previous Coin objects will be updated.

    """
    if rebuild():
        coins = create_coins("coins.txt")

        with open('coinList.pickle', 'wb') as file:
            pickle.dump(coins, file)


if __name__ == "__main__":
    run()
