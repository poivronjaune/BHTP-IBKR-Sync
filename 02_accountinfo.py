from ib_async import *

ib = IB()
connect_id = 102
ib.connect('127.0.0.1', 4002, clientId=connect_id)

# Get account summary
account = ib.managedAccounts()[0]       # returns a list of account strings, usually only one element hence [0]
summary = ib.accountSummary(account)    # 
for item in summary:
    print(f"{item.tag}: {item.value}")

ib.disconnect()
