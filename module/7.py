#!/usr/bin/env python3
#github.com/AngelSecurityTeam/Entrust
import requests
import optparse
from optparse import OptionParser
import re
import sys

parser = OptionParser()
parser.add_option("-d", "--domain", help="Domain to search")
(options, args) = parser.parse_args()

domain = options.domain

url = 'https://ctsearch.entrust.com/api/v1/certificates?fields=subjectDN&domain=%s&includeExpired=false&exactMatch=false&limit=5000' % domain

useragent = 'Mozilla/5.0 (X11; Linux i686; rv:75.0) Gecko/20100101 Firefox/75.0'

headers = {'User-Agent': useragent}

try:
    print("")
    response = requests.get(url, headers=headers)
    dmlist1 = re.findall(r'subjectDN": "cn\\u003d[a-zA-Z0-9.\-]{1,}', response.text)
    dmlist2 = []

    for i in dmlist1:
        x = re.sub("subjectDN\": \"cn\\\\u003d",'',i)
        dmlist2.append(x)

    dmset = set(dmlist2)
    counter = 0


    for i in dmset:
        counter = counter + 1
        print("\033[1;39m%s. %s" % (str(counter), str(i)))

    print("")

except Exception as e:
    print(e)
