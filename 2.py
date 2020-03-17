
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#https://github.com/AngelSecurityTeam/SubDomainExt

import requests
print("""
\033[1;35m
 _____       _    ______                      _       _____     _   
/  ___|     | |   |  _  \                    (_)     |  ___|   | |  
\ `--. _   _| |__ | | | |___  _ __ ___   __ _ _ _ __ | |____  _| |_ 
 `--. \ | | | '_ \| | | / _ \| '_ ` _ \ / _` | | '_ \|  __\ \/ / __|
\033[1;39m/\__/ / |_| | |_) | |/ / (_) | | | | | | (_| | | | | | |___>  <| |_ \033[1;35m
\033[1;39m\____/ \__,_|_.__/|___/ \___/|_| |_| |_|\__,_|_|_| |_\____/_/\_\\__|\033[1;35m
                                                 AngelSecurityTeam                                                    
""")                                                                    
                                                                    



website = input("Website : \033[1;39m")
print ("")

def main(website):
	url = "https://api.indoxploit.or.id/domain/{}".format(website)
	data = requests.get(url).json()
	ambil_data = data['data']['subdomains']
	for i in ambil_data:
		print(i)

if __name__ == '__main__':
	main(website)
