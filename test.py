"""
---ASTRA RESEARCH---

API client for PAYEER trading
Example "ticker24"
"""

import requests
import time
import json


res = requests.request(method='POST', url='https://payeer.com/api/trade/time')
#print(res.text)
current_rates = json.loads(res.text)
print (current_rates)

time=float(current_rates['time'])


print('timeServ=', time)
"""
print('ask24 =', ask)
print('last =', last)
print('min24 =', min24)
print('max24 =', max24)

"""