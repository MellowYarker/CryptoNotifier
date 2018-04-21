#!/usr/bin/env python3
"""
Where the program is run.

"""
import collect
from request import Bot
import time
import pickle
from notifications.Notification import PriceNotification, TradeNotification
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

            # Alerts!
            # TODO: CREATE A LIST OF ALERTS AND TRIGGER ALL THOSE AT ONCE
            alerts = []
            buy_alert = coin.buy_notifiaction()
            sell_alert = coin.sell_notification()

            if buy_alert or sell_alert:
                noti = TradeNotification(coin)
                noti.set_message()
                alerts.append(noti)

            price_alert = coin.price_notification()
            # if the price broke the threshold make a price_alert
            if price_alert != 0:
                noti = PriceNotification(coin, price_alert)
                noti.set_message()
                alerts.append(noti)
                # noti.notify()
                # time between notifications
            for alert in alerts:
                alert.notify()
                time.sleep(5)
            alerts = []

        time.sleep(bot.update_frequency())
