from ib_async import *

ib = IB()
connect_id = 107
ib.connect('127.0.0.1', 4002, clientId=connect_id)

# --- Cancel all open orders ---
open_orders = ib.openOrders()
for o in open_orders:
    ib.cancelOrder(o)
    print(f"Cancelled order: {o.action} {o.totalQuantity} {o.orderType}")

# --- Close all positions ---
positions = ib.positions()
for pos in positions:
    contract = pos.contract
    position_size = pos.position
    
    if position_size != 0:
        if position_size > 0:
            action = 'SELL'
        else:
            action = 'BUY'
        order_size = abs(position_size)
        
        ib.reqMktData(contract)
        ticker = ib.ticker(contract)
        ib.sleep(2)
        market_price = ticker.last if ticker.last else ticker.close
        
        if action == 'SELL':
            lmt_price = market_price * 0.98
        else:
            lmt_price = market_price * 1.02

        order = LimitOrder(action, order_size, lmt_price)
        order.outsideRth = True  # Allow execution outside regular trading hours
        order.exchange = 'ARCA' 
        
        trade = ib.placeOrder(contract, order)
        print(f"Placed limit order to {action} {order_size} shares of {contract.symbol} with after hours trading at price {lmt_price}...")

        while not trade.isDone():   
            ib.sleep(1)
            print(f"Order status: {trade.orderStatus.status}")


ib.disconnect()
