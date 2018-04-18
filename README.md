# Crypto Notifier
### A program that sends crypto price alerts via push notifications on Macs.

![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/grsExample.png "Example Notification")

This program uses the free CoinMarketCap.com [api](https://coinmarketcap.com/api/), all data is pulled from there.


## REQUIREMENTS
  * A Mac (this uses the MacOS notification center)
  * [Python 3.6+](https://www.python.org/downloads/release/python-365/)
  * open a terminal and navigate to CryptoNotifier/install
    * `$ sh dependencies.sh`
    * if this fails:
      * `$ sh retry.sh`


###### How to use it
1. open the coins.txt file, add the coins you want to recieve updates on.

   syntax for this file is as follows:

      coin ID, coin symbol, volume percentage change, price percentage change

      ex: bitcoin, BTC, 5, 5

   Volume analysis is being built still. If the price change is 5, it means (+/-) 5%
     * The option to have individual increase and decrease thresholds is being built.

2. open settings.txt

    The settings file (settings.txt) currently has 3 options:

        - the fiat currency you'd like to see prices listed in.

            - CAD, USD, EUR, etc

            - you can only choose one.

        - the time period for the change in price

            - hourly

            - daily (24 hours)

            - weekly (7 days)

            - you can only choose one (for now)

        - how often you want the bot to scan CMC

            - this is an integer, ex. 10 = 10 minutes

    Here's an example of a setup in settings.txt:

    CAD

    daily

    30

    This setup converts to Canadian dollars, uses the 24 hour price as a threshold,
    and scans coinmarketcap.com every 30 minutes.

3. open terminal and navigate to the CryptoNotifier directory.
  * python3 main.py

## Notes
This tool isn't complete, I just wanted to put it up because basic alerts do work. The code is kind of sketchy but I haven't used python in a few months, I'll fix that and the documentation over the next few weeks.

feel free to donate if you'd like :)

BTC: 12czBbxm5teNqo26tB9EFYs2U6tfajDQqD

GRS: FoCWRhe5CTJJwBPjtKy939ACB4S7ymU27Z


