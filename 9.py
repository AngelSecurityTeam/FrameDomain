#!/usr/bin/env python3
#ANgelsecurityTeam - DNSDUMPESTER
import sys
import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import urllib.parse
import re
import os
def getcsrf(t):
	d=t[(t.find("csrf")+28):(t.find("csrf")+60)]
	return d
total=[]
def eliminate(l):
        if(l not in total):
                total.append(l)
                
url="https://dnsdumpster.com/"
print('''\033[1;39m''')
dom=input("Domain: ")
print ('''  ''')
r=requests.get(url)
t=r.text
tkn="csrftoken="+getcsrf(t)+";"
header = {"Referer":"https://dnsdumpster.com","Cookie" :tkn}
r=requests.post("https://dnsdumpster.com",data={'csrfmiddlewaretoken':getcsrf(t),'targetip':dom},headers=header)
resp=r.text
l=re.findall((r'<tr><td class="col-md-4">(.*?).'+dom+'<br>'),resp)
for i in l:
        if(i!=''):
                v=i+'.'+dom
                eliminate(v)
                                             
link=[]
url="https://www.virustotal.com/en/domain/"+dom+"/information/"
r=requests.get(url)
t=r.text
f=open(".Angel.txt","w")
f.write(t)
f.write("Angel")
f.close()
f=open(".Angel.txt","r")
a="/"
n=0
for i in f.readlines():
           if i=="  <div class=\"enum \">\n":
                                            f.readline()
                                            a=f.readline()
                                            a.lstrip()
                                            if(a[-3:-1]=="om"):
                                                               
                                                               link=link+[a[100:-100]]
                                                               n+=1
for i in link:
    eliminate(i)
for i in total:
        print(i)
        


