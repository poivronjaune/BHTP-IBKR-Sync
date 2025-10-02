
import pandas as pd
from datetime import datetime
from ib_async import *

ib = IB()
connect_id = 103
ib.connect('127.0.0.1', 4002, clientId=connect_id)

contract = Stock("AAPL", "SMART", "USD")                    # Step 1 : Define a contract object for which to fetch data (stocks in this case)

bars = ib.reqHistoricalData(                                # Step 2 : request historical data for the last day in 1 minute bars (limitations apply, 1 minute => about 1 month)
    contract,
    endDateTime="",
    durationStr="1 D",
    barSizeSetting="1 min",
    whatToShow="TRADES",
    useRTH=False                                            # When useRTH (regular trading hours) is False, it will return all available data including pre-market and after-hours
)

df = util.df(bars)
print(df.head())
df.to_csv(f"AAPL_1min_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", index=False)

ib.disconnect()
