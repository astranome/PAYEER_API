"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "Sell 0.01 LTC Market order"
"""

import requests
import hashlib
import hmac
import time
import json


APISECRRET='Meow_55EXE ' #  SECRET on PAYEER API-TRADE (NOT MERCHANT!!!)
APIID='f390722b-8020-4289-8c2e-23123132312' #  ID on PAYEER API-TRADE (NOT MERCHANT!!!)
pair = "LTC_USD"
amount = "0.01"
ts = int(round(time.time()*1000))
ts=str(ts)
print(ts)
values =json.dumps ({
    "pair": pair,
    "type": "market",
    "action": "sell",
    "amount": amount,
    "ts": ts
  })
print(values)
msg = bytes(values, "utf-8")
method = 'order_create'
method = bytes(method, "utf-8")
api_secret = bytes(APISECRRET, "utf-8")
H = hmac.new(api_secret, digestmod=hashlib.sha256)
H.update(method)
H.update(msg)
sign = H.hexdigest()

headers = {
  'Content-Type': 'application/json',
  'API-ID': APIID,
  'API-SIGN': sign
}
print(headers)
res = requests.request(method= 'POST', url='https://payeer.com/api/trade/order_create', data=values, headers=headers)
print(res.text)

