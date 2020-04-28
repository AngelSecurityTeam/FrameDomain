#!/bin/bash
#https://github.com/AngelSecurityTeam

case $1 in
         
        -cert ) curl -s "https://jldc.me/anubis/subdomains/$2"|jq -r "." |grep -o "\w.*$2"
esac
