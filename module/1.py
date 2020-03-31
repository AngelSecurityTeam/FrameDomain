#!/usr/bin/env python3
#https://github.com/AngelSecurityTeam/

import sys
import urllib.request
import urllib.parse
import re
print("""

\033[1;35m   _____       __    ______     __                  __            
  / ___/__  __/ /_  / ____/  __/ /__________ ______/ /_____  _____
  \__ \/ / / / __ \/ __/ | |/_/ __/ ___/ __ `/ ___/ __/ __ \/ ___/
\033[1;39m ___/ / /_/ / /_/ / /____>  </ /_/ /  / /_/ / /__/ /_/ /_/ / /\033[1;35m    
\033[1;39m/____/\__,_/_.___/_____/_/|_|\__/_/   \__,_/\___/\__/\____/_/    \033[1;35m 
                                           AngelSecurityTeam v2 \033[1;39m 
                        
""")

if len(sys.argv) == 1:
	print("Usage: " + sys.argv[0] + " example.com ")
	sys.exit(1)

for i, arg in enumerate(sys.argv, 1):
	domains = set()
	with urllib.request.urlopen('https://crt.sh/?q=' + urllib.parse.quote('%.' + arg)) as r:
		code = r.read().decode('utf-8')
		for cert, domain in re.findall('<tr>(?:\s|\S)*?href="\?id=([0-9]+?)"(?:\s|\S)*?<td>([*_a-zA-Z0-9.-]+?\.' + re.escape(arg) + ')</td>(?:\s|\S)*?</tr>', code, re.IGNORECASE):
			domain = domain.split('@')[-1]
			if not domain in domains:
				domains.add(domain)
				print(domain)
