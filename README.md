# Crypto Notifier
### A program that displays crypto price alerts via push notifications on Macs.

![alt text](https://github.com/MellowYarker/CryptoNotifier/blob/master/images/grsExample.png "Example Notification")

This program uses the free CoinMarketCap.com [api](https://coinmarketcap.com/api/), if the coin you're looking for isn't there then there won't be data for it.


## REQUIREMENTS
  * A Mac (this uses the MacOS notification center)
  * [Python 3.6+](https://www.python.org/downloads/release/python-365/)
  * Clone this repo to download it then open a terminal and navigate to CryptoNotifier/install
    * `$ sh dependencies.sh`
    * if the dependencies script fails, try:
      * `$ sh retry.sh`
    * if this also fails, see if you have pip or pip3 installed, if not [install it](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)



##### Instructions
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

            - you can only choose one.

        - the time period for the change in price

            - hourly

            - daily (24 hours)

            - weekly (7 days)

            - you can only choose one (for now)

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
This tool isn't complete, I just wanted to put it up because basic alerts work. The code and documentation need work but it's pretty extendible so that's good.

feel free to donate if you'd like :)

BTC: 12czBbxm5teNqo26tB9EFYs2U6tfajDQqD

GRS: FoCWRhe5CTJJwBPjtKy939ACB4S7ymU27Z

XLM: GAY7TEP5OCGHB37RBE3KJIYRQO7FPSL5GZRE6VIBZVXKOPQOFDEUB2W4


