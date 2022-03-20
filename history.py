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
#ts=str(ts)
print("PAIR:", pair)
print("NOW:", time.strftime("%c", time.gmtime()))
values =json.dumps ({"pair": pair})


headers = {'Content-Type': 'application/json'}
#print(headers)
res = requests.request(method='POST', url='https://payeer.com/api/trade/trades', data=values, headers=headers)
#print(res.text)

dt=json.loads(res.text)#; print  (dt)

dt =dt['pairs'][pair]; print("Last ", len(dt), " trades info:")
s=0
for a in range(len(dt)):
    s = s + float(dt[a]['amount'])
print ('amount sum :', s)
l=0
for b in range(len(dt)):
    l = l + float(dt[b]['value'])
print ('value sum :', l)
print ('average price :', l/s)
tm=(dt[0]['date'])

#print(time.gmtime(int(tm)))

print("Last TRADE was:", time.strftime("%c", time.gmtime(tm)))