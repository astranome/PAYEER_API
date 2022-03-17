"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "BYU 10 TRX Market order"
"""

import requests
import time
import json

pair = "LTC_USD"

ts = int(round(time.time()*1000))
ts=str(ts)
print(ts)

values =json.dumps ({"pair": pair})


headers = {'Content-Type': 'application/json'}
print(headers)
res = requests.request(method='POST', url='https://payeer.com/api/trade/ticker', data=values, headers=headers)
print(res.text)



