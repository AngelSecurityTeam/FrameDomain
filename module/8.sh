#!/bin/bash
#https://github.com/AngelSecurityTeam

case $1 in
         
        -cert ) curl -s "https://riddler.io/search/exportcsv?q=pld:$2"|cut -d "," -f6|grep $2
esac
