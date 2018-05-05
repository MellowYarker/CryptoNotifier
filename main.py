#!/usr/bin/env python3
"""
Where the program is run.

"""
import collect
from request import Scraper
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
        scrape = Scraper(coins)
        for coin in scrape.coins:
            result = scrape.request_coin(coin.id)
            parser.parse(coin, result)

            # Alerts!
            # this is a list of all alerts for this coin
            alerts = []
            buy_alert = coin.buy_notification()
            # TODO: Build sell notification in Coin class
            sell_alert = coin.sell_notification()

            if buy_alert or sell_alert:
                noti = TradeNotification(coin)
                noti.set_message()
                alerts.append(noti)

            change_alert = coin.change_notification()
            # if the price broke the threshold make a change_alert
            if change_alert != 0:
                noti = PriceNotification(coin, change_alert)
                noti.set_message()
                alerts.append(noti)
            for alert in alerts:
                alert.notify()
                # time between notifications
                time.sleep(5)
            alerts = []

        time.sleep(scrape.update_frequency())
