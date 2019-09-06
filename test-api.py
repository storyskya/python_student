#!/bin/python

import requests
import json

# url = 'http://ip.taobao.com/service/getIpInfo.php?ip='
# city = '58.83.237.41'
# ret = requests.get(url + city)


# d = ret.json()
# x = json.dumps(d)
# print(x)
# with open('tianqi.json','w') as f:
#     json.dump(d,f)

with open('tianqi.json','r') as u:
    x = json.load(u)

# print(json.dumps(x['data']['country'],indent=2,separators=(',',':')))

def find_ip(max):
    try:
        ip_dict = max['data']
        for ip_name,ip_data in ip_dict.items():
            print(ip_name,':',ip_data)
    except Exception as e:
        print(e)
find_ip(x)
# print(d['data']['country'])