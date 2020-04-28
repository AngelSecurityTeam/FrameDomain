#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#https://github.com/AngelSecurityTeam/SubDomainExt

import requests
website = input("\n\033[1;39mWebsite : \033[1;39m")
print ("\033[1;39m")

def main(website):
	url = "https://api.indoxploit.or.id/domain/{}".format(website)
	data = requests.get(url).json()
	ambil_data = data['data']['subdomains']
	for i in ambil_data:
		print(i)

if __name__ == '__main__':
	main(website)
