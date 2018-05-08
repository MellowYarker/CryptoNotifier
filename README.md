# Crypto Notifier
### A program that displays crypto price alerts via push notifications on Macs.

## REQUIREMENTS
  * A Mac (this uses the MacOS notification center)
  * [Python 3.6+](https://www.python.org/downloads/release/python-365/)
  * A little patience and a bit of familiarity with the [command line](https://www.davidbaumgold.com/tutorials/command-line/).

![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/better.gif "Example GIF")

## Note
Thanks to this I've pretty much stopped looking at my portfolio on apps and websites (whereas before I checked multiple times an hour). This program isn't built to update you on the price of your holdings every 3 seconds, I like using it to let me know when there's been a notable change in price like +15% in the last day or if a coin's price has fallen to a point where I'd like to buy it. I hope this helps you as much as it's helped me.

Here's a quick list of the types of notifications **currently supported**:

* **Price percent change**: Be notified when the price increases x% or decreases y%
* **Buy alert**: If the price of a coin costs $10 and you want to buy it at $10 or less, you get a notification.
* **Sell alert**: If the price of a coin costs $40 and you want to sell it at $40 or more, you get a notification.

You can choose the fiat currency you'd like prices to be displayed in, how often you want to *scan* coinmarketcap.com, and the time frame between price changes. Ex: 24 hour change in price.

*Coming soon*

* **Volume alert**: If the volume is high enough for you to buy or sell a large quantity of coins then you get a notification.

![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/grsExample.png "Example Notification")

This program uses the free CoinMarketCap.com [api](https://coinmarketcap.com/api/), if the coin you're looking for isn't there then there won't be data for it.


## Set up
  1. Clone this repo to download it (found at the top right of this page).
  ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/clone.png "Clone")
  2. Open finder and navigate to wherever you downloaded this program.
    * Once there, open the `CryptoNotifier-master` folder.
  3. Press command + spacebar
    * Type `terminal` and press enter.

  4. In the terminal, type `cd ` (with a space after, so "cd "), go back to finder and drag the `install` folder into the terminal.

  ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/finder_terminal.png "Finder and Terminal")

  ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/dragged.png "Dragged In")

    Once the filepath is displayed press enter.

  ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/directory.png "Directory")
  5. If you've installed python 3.6 or higher, type `python3 setup.py` in the terminal. If not, check the requirements heading.

  **If this fails**, see if you have pip or pip3 installed by typing `which -a pip` or `which -a pip3`, if not [install it](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)


### A Quick Example
1. If coming from **set up** type `cd ../` in the terminal then go to step 2
* **OTHERWISE**
1. Open a terminal and navigate to the *CryptoNotifier-master* directory.

2. Type `python3 main.py`

3. There should be notifications for bitcoin and litecoin (you can change these below).



#### Instructions
1. Open **settings.txt**

    The settings file (settings.txt) currently has 3 options:

        - The fiat currency you'd like to see prices listed in.

            - CAD, USD, EUR, etc

            - You can only choose one.

        - The time period for the change in price

            - Hourly

            - Daily (24 hours)

            - Weekly (7 days)

            - You can only choose one

        - How often you want the scraper to scan CMC

            - This is an integer, ex. 10 = 10 minutes

    Here's an example of a setup in settings.txt:

    ```
    CAD
    daily
    30
    ```

    This setup converts to Canadian dollars, watches the 24 hour price change,
    and scans coinmarketcap.com every 30 minutes.

2. Open **coins.txt**, *the coins there now are just examples*.
    * Add the coins you want to receive updates on, syntax for this file is as follows:

      **coin ID**, **coin symbol**, **buy price**, **sell price**, **percent increase**, **percent decrease**

      **ex**: bitcoin, BTC, 8000, 20000, 10, -10

   An example set up:

   ![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/exampleCoins.png "Coin Setup")

3. Open a terminal and navigate to the *CryptoNotifier-master* directory.
  * `python3 main.py`

That's it, just let it run in the background (**don't close the terminal**) and go on about your day.
**If you want to change the coins or settings**, just change the files (as described in the instructions) and save them.

* You can re-run the program from the terminal if you'd like to scan right away, but it checks if coins.txt or settings.txt have changed between scans so it's not necessary.

### IMPORTANT
If this program crashes, you probably won't know until you check the terminal for an error message. Aside from crashing due to formatting errors in the settings (*which you'll know about right away*) it can crash if you scan without an internet connection (I guess theoretically it would crash if coinmarketcap.com was down).

* I've tried sending a push notification (*request.py* line 121) to alert the user if the program crashed but it doesn't work, another work-around I've considered is sending a notification every now and then alerting the user that the program is running.

Feel free to donate if you'd like :)

BTC: 12czBbxm5teNqo26tB9EFYs2U6tfajDQqD

GRS: FoCWRhe5CTJJwBPjtKy939ACB4S7ymU27Z

Stellar: GAY7TEP5OCGHB37RBE3KJIYRQO7FPSL5GZRE6VIBZVXKOPQOFDEUB2W4
