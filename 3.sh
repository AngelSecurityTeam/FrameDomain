#!/bin/bash
#https://github.com/AngelSecurityTeam

case $1 in
         
	-cert ) curl -s "https://dns.bufferover.run/dns?q=."$2 | jq -r .FDNS_A[]|cut -d',' -f2|sort -u | grep $2
esac
