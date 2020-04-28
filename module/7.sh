#!/bin/bash
#https://github.com/AngelSecurityTeam

case $1 in
         
        -cert ) curl -s "https://api.threatminer.org/v2/domain.php?q=$2&rt=5" | jq -r '.results[]'  |grep -o "\w.*$2"
esac
