#!/bin/bash
# Source function library. 
. /etc/rc.d/init.d/functions

awk -F '[<>.]' '/[0-9]+\.[0-9]+\.[0-9]+\./{print $3"."$4"."$5}' "/data1/script/pt_proxy.source" |sort |uniq -c |sort > /data1/script/pt_proxy.list
awk -F '[<>.]' '/[0-9]+\.[0-9]+\.[0-9]+\./{print $3"."$4"."$5}' "/data1/script/gn_proxy.source" |sort |uniq -c |sort > /data1/script/gn_proxy.list

pt_proxy()
{    for i in `seq 1 647`
    do
      curl -s http://www.xicidaili.com/nt/"$i" |awk -F '[<>.]' '/[0-9]+\.[0-9]+\.[0-9]+\./' >> "/data1/script/pt_proxy.source"
      sleep 3
    done
}

gn_proxy()
{
    for i in `seq 1 2750`
    do
      curl -s http://www.xicidaili.com/nn/"$i" |awk -F '[<>.]' '/[0-9]+\.[0-9]+\.[0-9]+\./' >> "/data1/script/gn_proxy.source"
      sleep 3
    done
}

make_list()
{
    ps aux|grep [c]url
    if [ $? -gt 0 ];then
        awk -F '[<>.]' '/[0-9]+\.[0-9]+\.[0-9]+\./{print $3"."$4"."$5}' "/data1/script/pt_proxy.source" |sort |uniq -c |sort > /data1/script/pt_proxy.list &
        awk -F '[<>.]' '/[0-9]+\.[0-9]+\.[0-9]+\./{print $3"."$4"."$5}' "/data1/script/gn_proxy.source" |sort |uniq -c |sort > /data1/script/gn_proxy.list &
    fi
}
case "$1" in
    start)
    pt_proxy &
    gn_proxy &
    ;;
    status)
    ps aux |awk '/[c]url/'
    ;;
    create)
    make_list
    ;;
    *)
    exit 1
    ;;

esac
exit 0