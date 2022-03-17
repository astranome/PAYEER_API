#https://payeer.com/api/trade/trades
"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "Trades"
"""

import requests
import time
import json

pair = "LTC_USD,DOGE_USD"

ts = int(round(time.time()*1000))
ts=str(ts)
print(ts)

values =json.dumps ({"pair": pair})


headers = {'Content-Type': 'application/json'}
print(headers)
res = requests.request(method='POST', url='https://payeer.com/api/trade/trades', data=values, headers=headers)
print(res.text)



