#!/bin/bash
while [[ true ]]; do
   netstat -n | awk -F'[:\t ]+' '/14.29.93.206:80/{print $6}' |awk -F"." '{print $1"."$2"."$3}' |sort |uniq -c |sort -nr |awk '$1>500 {print $2}' > /tmp/denylist.txt
   for i in `cat /tmp/denylist.txt`
       do
           /sbin/iptables -L -n | grep "$i"
           if [ $? -gt 0 ];then
              /sbin/iptables -I INPUT -s "$i"".0/24" -p tcp --dport 80 -j DROP
              echo $i >> /data1/script/denylist.txt
           fi
       done
       sleep 60
done


while [[ true ]]; do
   netstat -n | awk -F'[:\t ]+' '/14.29.93.206:80/{print $6}' |sort |uniq -c |sort -nr |awk '$1>500 {print $2}' > /tmp/denylist.txt

#!/bin/bash
netstat -n | awk -F'[:\t ]+' '/14.29.93.206:80/{print $6}' |awk -F"." '{print $1"."$2"."$3}' |sort |uniq -c |sort -nr |awk '$1>300 {print $2}' > /tmp/denylist.txt
for i in `cat /tmp/denylist.txt`
    do
        /sbin/iptables -L -n | grep "$i"
        if [ $? -gt 0 ];then
           /sbin/iptables -I INPUT -s "$i"".0/24" -p tcp --dport 80 -j DROP
           echo $i >> /data1/script/denylist.txt
        fi
    done

#!/bin/bash
netstat -n |grep "14.29.93.206:80" > /data1/script/netstat.log
/sbin/iptables -L -n > /data1/script/iptables_list.log
gn_list="/data1/script/gn_proxy.list"
pt_list="/data1/script/pt_proxy.list"
for p in `cat "$gn_list" "$pt_list"`
    do
        grep "$p" /data1/script/iptables_list.log
        if [ $? -gt 0 ];then
            grep "$p" /data1/script/netstat.log
            if [ $? == 0 ];then
                /sbin/iptables -I INPUT -s "$p"".0/24" -p tcp --dport 80 -j DROP
                echo $p >> /data1/script/denylist.txt
            fi
        fi
done