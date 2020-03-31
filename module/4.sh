#!/bin/bash
#https://github.com/AngelSecurityTeam

case $1 in
         
	-cert ) curl -s "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=$2"|jq .subdomains|grep -o "\w.*$2"
esac
