"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "BYU 10 TRX Market order"
"""

import requests
import hashlib
import hmac
import time
import json


APISECRRET='MY_SECRET' # ---CHANGE IT 
APIID='MY_ID-8c2e-57b86eee88ab' # Change Too :-)
pair = "TRX_USD"
amount = "10"
ts = int(round(time.time()*1000))
ts=str(ts)
print(ts)
values =json.dumps ({
    "pair": pair,
    "type": "market",
    "action": "buy",
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

