#!/usr/bin/env python3
"""
Where the program is run.

"""
import collect
from request import Bot
import time
import pickle
from notifications.Notification import PriceNotification
import parser


if __name__ == "__main__":
    while True:
        # search the coins.txt and settings.txt files for updates
        collect.run()

        with open("coinList.pickle", "rb") as f:
            coins = pickle.load(f)
        # Request data for each coin
        bot = Bot(coins)
        for coin in bot.coins:
            result = bot.request_coin(coin.id)
            parser.parse(coin, result)
            alert = coin.price_notification()
            # if the price broke the threshold make an alert
            if alert != 0:
                noti = PriceNotification(coin, alert)
                noti.set_message()
                noti.notify()
                # time between notifications
                time.sleep(5)

        time.sleep(bot.update_frequency())
