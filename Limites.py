"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "ticker24"
"""

import requests
import time
import json

pair = "DOGE_USD"

ts = int(round(time.time()*1000))
ts=str(ts)
#print(ts)

values =json.dumps ({"pair": pair})
headers = {'Content-Type': 'application/json'}
#print(headers)
res = requests.request(method='POST', url='https://payeer.com/api/trade/info', data=values, headers=headers)
#print(res.text)
current_rates = json.loads(res.text)
print (current_rates)
min_amount=float(current_rates['pairs'][pair]['min_amount'])
min_value=float(current_rates['pairs'][pair]['min_value'])
fee_maker_percent=float(current_rates['pairs'][pair]['fee_maker_percent'])
fee_taker_percent=float(current_rates['pairs'][pair]['fee_taker_percent'])

print('Limits for ', pair)
print('min_amount=', min_amount)
print('min_value =', min_value)
print('fee_maker_percent =', fee_maker_percent)
print('fee_taker_percent =', fee_taker_percent)





