#!/bin/bash
#https://github.com/AngelSecurityTeam

case $1 in
         
        -cert ) curl -s "https://otx.alienvault.com/api/v1/indicators/domain/$2/passive_dns"|jq '.passive_dns[].hostname' |grep -o "\w.*$2"
esac
