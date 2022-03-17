"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "Ticker statistic 24 orders"
"""


import requests
import time
import json

pair = "LTC_USD"

ts = int(round(time.time()*1000))
ts=str(ts)
#print(ts)

values =json.dumps ({"pair": pair})


headers = {'Content-Type': 'application/json'}
#print(headers)
res = requests.request(method='POST', url='https://payeer.com/api/trade/ticker', data=values, headers=headers)
#print(res.text)
current_rates = json.loads(res.text)
print (current_rates)
bid=float(current_rates['pairs']['LTC_USD']['bid'])
ask=float(current_rates['pairs']['LTC_USD']['ask'])
last=float(current_rates['pairs']['LTC_USD']['last'])
min24=float(current_rates['pairs']['LTC_USD']['min24'])
max24=float(current_rates['pairs']['LTC_USD']['max24'])

print('bid24=', bid)
print('ask24 =', ask)
print('last =', last)
print('min24 =', min24)
print('max24 =', max24)



