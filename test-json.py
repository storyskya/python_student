#!/bin/python

import json

d = {
    'name':'d8g',
    'city':'beijing',
    'noney':[1,3,5,6]
}

with open('test.json','w') as f:
    r = json.dump(d,f)

with open('test.json','r') as u:
    x = json.load(u)



print(x)
print(json.dumps(x))
w = json.dumps(x)
print(w)
print(json.loads(w))

print(json.dumps(x,indent=2,separators=(',',':')))