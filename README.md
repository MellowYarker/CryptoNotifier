# Crypto Notifier
### A program that displays crypto price alerts via push notifications on Macs.

* I built this for people (me, really), not bots. Thanks to this I've virtually stopped looking at my portfolio on apps and websites (whereas before I checked it multiple times an hour). This program isn't built to update you on the price of your holdings every 3 seconds, I like using it to let me know when there's been a noteable change in price, for example +15% in the last day.

Here's a quick list of the types of notifications **currently supported**:

    * Price percent change: If the price changes x% in the last (hour, day, week), there's a notification.
    * Buy alert: If the price of a coin costs $10 and you want to buy it at $10 or less, you get a notification.

*Coming soon*

    * Positive/negative price percent change: Instead of (+/-) 15%, you can set up notifications for +15% and -30%
    * Sell alert: If the price of a coin costs $40 and you want to sell it at $40 or more, you get a notification.
    * Volume alert: If the volume is high enough for you to buy or sell a large quantity of coins then you get a notification.

![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/grsExample.png "Example Notification")

This program uses the free CoinMarketCap.com [api](https://coinmarketcap.com/api/), if the coin you're looking for isn't there then there won't be data for it.


## REQUIREMENTS
  * A Mac (this uses the MacOS notification center)
  * [Python 3.6+](https://www.python.org/downloads/release/python-365/)


## Set up
  1. Clone this repo to download it.
  ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/clone.png "Clone")
  2. Open finder and navigate to wherever you downloaded this program.
    * Once there, open the `CryptoNotifier` folder.
  3. Press command + spacebar
    * Type `terminal` and press enter.

  ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/finder_terminal.png "Finder and Terminal")
  4. In terminal, type `cd ` (with a space after, so "cd "), go back to finder and drag the `install` folder into the terminal.

  ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/dragged.png "Dragged In")
    * Once the filepath is displayed press enter.

    ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/directory.png "Directory")
  5. If you've installed python 3.6 or higher, type `python3 setup.py` in the terminal. If not, check the requirements heading.
        * if this fails, see if you have pip or pip3 installed by typing `which -a pip` or `which -a pip3`, if not [install it](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)



#### Instructions
1. Open coins.txt file,
    * Add the coins you want to recieve updates on, syntax for this file is as follows:

      coin ID, coin symbol, buy price, price percentage change

      ex: bitcoin, BTC, 8000, 5

   If the price change is 5, it means (+/-) 5%
     * **(note)** The option to have individual increase and decrease thresholds is being built.
   Assume we want everything relative to the Canadian dollar (CAD) (**this is determined in the settings file**), according to the chosen buy price, if bitcoin is worth $8000 CAD there will be a buy alert.

2. open settings.txt

    The settings file (settings.txt) currently has 3 options:

        - the fiat currency you'd like to see prices listed in.

            - CAD, USD, EUR, etc

            - you can only choose **one**.

        - the time period for the change in price

            - hourly

            - daily (24 hours)

            - weekly (7 days)

            - you can only choose **one**

        - how often you want the scraper to scan CMC

            - this is an integer, ex. 10 = 10 minutes

    Here's an example of a setup in settings.txt:

    ```
    CAD
    daily
    30
    ```

    This setup converts to Canadian dollars, watches the 24 hour price change,
    and scans coinmarketcap.com every 30 minutes.

3. open terminal and navigate to the CryptoNotifier directory.
  * `python3 main.py`

## Notes
This tool isn't complete, I just wanted to put it up because basic alerts work. Working on documentaion and a few other notifications and features. Not planning on writing any tests for this outside the occasional doctest.

feel free to donate if you'd like :)

BTC: 12czBbxm5teNqo26tB9EFYs2U6tfajDQqD

GRS: FoCWRhe5CTJJwBPjtKy939ACB4S7ymU27Z

XLM: GAY7TEP5OCGHB37RBE3KJIYRQO7FPSL5GZRE6VIBZVXKOPQOFDEUB2W4


