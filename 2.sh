#!/bin/bash
#https://github.com/AngelSecurityTeam

case $1 in
     
	-cert ) curl -s https://certspotter.com/api/v0/certs\?domain\=$2 | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $2

esac
