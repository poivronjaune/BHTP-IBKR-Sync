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

# Running the samples
If you just started the ib_gatway desktop application on your system, a status window should be shown with no client connections.  

| Sample | Description | Result |
|---|---|---|
| n.a. | Initial launch of ib_gateway desktop application should show an empty conected clients window  | <img src="img\run_01a.png" width="350"> |
| 01_connect.py | This script connects to the ib_gateway with client id 101. When ENTER is pressed it simply disconnects. | <img src="img\run_01b.png" width="350"> |
| 02_accountinfo.py | This script will connect with a new client id (102) and will retreive your account.<br><br>The terminal console should display your existing bying power (example for a single account in IBKR) | <img src="img\run_02a.png" width="350"><br><br><img src="img\run_02b.png" width="350"> |
| 03_historicaldata.py | This script will connect to ib_gateway with client id 103 and retrieve 1 day of historical minute price data, convert it to a PANDAS dataframe and display the first five rows | <img src="img\run_03a.png" width="350"><br><br><img src="img\run_03b.png" width="350"> |
|  |  |  |
|  |  |  |
|  |  |  |





