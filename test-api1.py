#!/bin/python
from bs4 import BeautifulSoup
import requests
import jieba
import collections

blog_url = 'https://blog.51cto.com/storysky/2065158'
data = requests.get(blog_url)
# print(data.text)
coutents = BeautifulSoup(data.text,'html.parser')
# print(coutents)
all_p = coutents.find_all('p')
all_text = ''
for p in all_p:
    # print(p.text)
    all_text += str(p.text)

text = jieba.cut(all_text)
text_list = []
for t in text:
    # print(t)
    text_list.append(t)
# print(text_list)
count = collections.Counter(text_list)

for key,val in count.most_common(10):
    print(key,val)
