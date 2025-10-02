from ib_async import IB

ib = IB()
connect_id = 101
ib.connect('127.0.0.1', 4002, clientId=connect_id)
print("Connected to ib_gateway")
print(f"Check the ib_gateway interface to see a tab with ID={connect_id}")
input("Press Enter to disconnect from ib_gateway...")

ib.disconnect()
