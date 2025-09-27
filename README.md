# BHTP-IBKR-Sync
Example Synchronous Python to interact with IB_Gateway (from interactive brokers) to get portfolio data, stock prices, historical data and screeners.

# Installation (Windows)
Download an install this repo
```
git clone https://github.com/poivronjaune/BHTP-IBKR-Sync.git
cd BHTP-IBKR-Sync
py -m venv env
env\scripts\activate
py -m pip install -U pip
pip install -r requirements.txt

```

# Interactive Broker's IB_Gateway
The python application will use a special package called [ib_async](https://github.com/ib-api-reloaded/ib_async) to connect to the interactive broker's API. 
Get the latest ib_gateway from [interactive broker's website](https://www.interactivebrokers.com/en/trading/ibgateway-latest.php)  

Another option called [Trader's Workstation](https://www.interactivebrokers.com/en/trading/tws.php) is available to implement the API like ib_gateway, but that tool is a fully functional trading platform and is more complicated to use.

# Configuration  
See the [ib_async github repo](https://github.com/ib-api-reloaded/ib_async) to view a detailed installation anad configuration process.  

Before launching the python application  
| Check this | Propable view |
|---|---|
| Make sure the ib_gateway is connect to interactive broker's servers.<br>All three services must be in the green state   | <img src="img\ibkr_01.png" width="250"> |
| Open the configure panel | <img src="img\ibkr_02.png" width="250"> |
| Goto the settings setion<br>Remove the Read-Only API checkbox<br>Grab the Socket port for your setup<br>Usually 4002 for ib_gateway | <img src="img\ibkr_03.png" width="350"> |

# First run



