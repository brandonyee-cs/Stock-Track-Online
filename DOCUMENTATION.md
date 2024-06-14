# Documentation
[Back to Read Me](https://github.com/brandonyee-cs/StockTrackOnline)

## Running Beta Services:
Clone the Repository

Change Directories into the Beta Directory
```
cd STO
```

Install Necessary Packages.
```
pip install -r requirements.txt
```

For this setup you need both an [Alpha Vantage API Key](https://www.alphavantage.co/), and a [Trading Economics API Key](https://tradingeconomics.com/).

Create the config folder
```
mkdir config && cat keys.json
```

Edit keys.json following the JSON template below:
```
{
    "AVA_key" : "{ALPHA VANTAGE API KEY}",
    "TEA_key" : "{TRADING ECONOMICS API KEY}"
}
```

Now you can use the STO functions.