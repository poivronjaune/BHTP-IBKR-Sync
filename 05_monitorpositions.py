from ib_async import *

ib = IB()
connect_id = 110
ib.connect('127.0.0.1', 4002, clientId=connect_id)

# --- Open Orders ---
open_orders = ib.openOrders()
print("Open Orders:")
if not open_orders:
    print("  None")
else:
    for o in open_orders:
        print(f"  {o.action} {o.totalQuantity} {o.orderType} {o.lmtPrice if hasattr(o, 'lmtPrice') else ''} {o.tif}")

# --- Trades / Status ---
print("\nTrades:")
for trade in ib.trades():
    #if trade.orderStatus.status != 'Filled':
    #    print(f"  {trade.contract.symbol}: {trade.orderStatus.status} Trade state: {trade.orderStatus.filled} remaining={trade.orderStatus.remaining}")
    print(trade)

# --- Positions ---
print("\nCurrent Positions:")
positions = ib.positions()
if not positions:
    print("  None")
else:
    for pos in positions:
        print(f"  {pos.contract.symbol}: {pos.position} @ {pos.avgCost}")

ib.disconnect()
