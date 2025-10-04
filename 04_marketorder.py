# Basic trade at market value, may not fulfill at expected price is high volatility
# Be careful using this type of order.
# Only works durintg regular trading hours
from ib_async import *

ib = IB()
connect_id = 104
ib.connect('127.0.0.1', 4002, clientId=connect_id)

# Create a contract and order
contract = Stock('AAPL', 'SMART', 'USD')
order = MarketOrder('BUY', 2)

# Place the order
trade = ib.placeOrder(contract, order)
print(f"Order placed: {trade}")

# Monitor order status
while not trade.isDone():
    ib.sleep(1)
    print(f"Order status: {trade.orderStatus.status}")

ib.disconnect()
