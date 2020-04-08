#!/usr/bin/env python3
#github.com/AngelSecurityTeam/SubIncanA # tool FrameDomain

import sys, requests, json, os, threading
from bs4 import BeautifulSoup as bs

def enterRes(e):
    e = e.split('/', 1)[0]

    if e not in result:
        result.append(e)

def enumHackertarget():


    r = requests.get('https://api.hackertarget.com/hostsearch/?q=' + domain).text
    e = r.split('\n')



    for i in e:
        enterRes(i.split(',')[0])


def enumPtrarchive():


    c = requests.Session()
    h = {
        'Referer': 'http://www.ptrarchive.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    t = {'pa_id': '1337'}



    r = c.get('http://www.ptrarchive.com/tools/search4.htm?label=' + domain + '&date=ALL', headers=h, cookies=t).text
    s = bs(r, 'html.parser')
    e = s.find('pre').text.split('\n')



    for i in e:
        e = i[i.find(']'):].split(' ')

        try:
            if e[1].endswith('.' + domain) and not e[1].startswith('*'):
                enterRes(e[1])
        except IndexError:
            pass


def enumCertspotter():


    r = requests.get('https://certspotter.com/api/v0/certs?domain=' + domain).text
    j = json.loads(r)



    for i in j:
        for e in i['dns_names']:
            if e.endswith('.' + domain) and not e.startswith('*'):
                enterRes(e)


def enumRiddler():


    r = requests.get('https://riddler.io/search?q=pld:' + domain).text
    s = bs(r, 'html.parser')
    e = s.findAll('td', class_='col-lg-5 col-md-5 col-sm-5')



    for i in e:
        enterRes(i.text.strip())


def enumCrt():


    r = requests.get('https://crt.sh/?q=%25' + domain).text
    s = bs(r, 'html.parser')

    try:
        e = s.findAll('table')[1].findAll('tr')
    except IndexError:
        print('')
    else:
        print('')

        for i in e:
            e = i.findAll('td')

            try:
                e = e[4].text

                if e.endswith('.' + domain) and not e.startswith('*'):
                    enterRes(e)
            except IndexError:
                pass


def enumSecuritytrails():


    r = requests.get('https://securitytrails.com/list/apex_domain/' + domain).text
    s = bs(r, 'html.parser')
    e = s.findAll('td')



    for i in e:
        e = i.find('a')

        if e:
            enterRes(e.text)


def enumThreatminer():


    try:
        r = requests.get('https://api.threatminer.org/v2/domain.php?q=' + domain + '&rt=5', timeout=6).text
        j = json.loads(r)



        for i in j['results']:
            enterRes(i)
    except requests.exceptions.Timeout:
        print('')
        pass


def enumVirustotal():


    r = requests.get('https://www.virustotal.com/ui/domains/' + domain + '/subdomains?limit=40').text
    j = json.loads(r)

    try:
        n = str(j['links']['next'])
        c = 1

        for i in j['data']:
            enterRes(i['id'])

        while type(n) is str:

            r = requests.get(n).text
            j = json.loads(r)

            for i in j['data']:
                enterRes(i['id'])

            try:
                n = str(j['links']['next'])
                c = c + 1
            except KeyError:
                break
    except KeyError:
        print('')

        for i in j['data']:
            enterRes(i['id'])


def enumThreatcrowd():


    r = requests.get('https://threatcrowd.org/searchApi/v2/domain/report/?domain=' + domain).text
    j = json.loads(r)



    if "subdomains" not in j:
        print("")
        return

    for e in j['subdomains']:
        enterRes(e)


def enumFindsubdomains():


    r = requests.get('https://findsubdomains.com/subdomains-of/' + domain).text
    s = bs(r, 'html.parser')
    e = s.findAll('td', {'data-field': 'Domain'})



    for i in e:
        if i.get('title'):
            enterRes(i.get('title'))


def enumDNSDumpster():


    c = requests.Session()
    r = c.get('https://dnsdumpster.com').text
    h = {'Referer': 'https://dnsdumpster.com'}
    t = c.cookies.get_dict()['csrftoken']



    r = c.post('https://dnsdumpster.com', data={'csrfmiddlewaretoken': t, 'targetip': domain}, headers=h).text
    s = bs(r, 'html.parser')
    t = s.findAll('table')[-1].findAll('td', class_='col-md-4')

    for i in t:
        t = i.text.split()[0]
        enterRes(t)
try:
    domain = sys.argv[1]
except IndexError:
    print('')
    sys.exit()

result = []
output = open('results/' + domain + '.txt', 'w')



functions = [
    enumDNSDumpster,
    enumFindsubdomains,
    enumThreatcrowd,
    enumThreatminer,
    enumVirustotal,
    enumSecuritytrails,
    enumHackertarget,
    enumCrt,
    enumCertspotter,
    enumRiddler,
    enumPtrarchive
]

threads = []

if __name__ == '__main__':

    for f in functions:
        t = threading.Thread(target=f)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

filtered = list(filter(None, result))

try:
    for i in filtered:
        output.write(i + '\n')
finally:
    output.close()


print("\033[1;39m")
os.system('cat results/' + domain + '.txt')

