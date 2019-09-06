#!/usr/bin/env python
# -*- coding=utf-8 -*-
# filename testlog.py
# author MaxD

import os
import re

base_dir = 'D:/python-start/'
log_path = os.path.join(base_dir,'logtmp.txt')
log_file = open(log_path)
log_data = log_file.readlines()
log_file.close()


status_dic = {}
for line in log_data:
    line_status = line.split(' ')[10]
    if line_status == '200':
        status_dic[line_status] = status_dic.get(line_status,0) + 1
print(status_dic)

re_ip = re.compile(r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)')
ip_dic = {}
for line in log_data:
    match = re_ip.match(line)
    if match:
        ip = match.group()
        ip_dic[ip] = ip_dic.get(ip,0) + 1
    print(ip_dic)