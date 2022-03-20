#https://payeer.com/api/trade/trades
"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "Trades"
"""

import requests
import time
import json

pair = "DOGE_USD"

ts = int(round(time.time()*1000))
ts=str(ts)
print(ts)

values =json.dumps ({"pair": pair})


headers = {'Content-Type': 'application/json'}
print(headers)
res = requests.request(method='POST', url='https://payeer.com/api/trade/trades', data=values, headers=headers)
print(res.text)

dt=json.loads(res.text); print  (dt)

'''
for item in dt:
    print(item)
for key, value in dt.items():
    print(key, value)
    
    print('---')
'''    
dt =dt['pairs'][pair]; print(len(dt))
s=0
for a in range(len(dt)):
    s = s + float(dt[a]['amount'])
print (a, s)
l=0
for b in range(len(dt)):
    l = l + float(dt[b]['value'])
print (b, l)
print (l/s)



