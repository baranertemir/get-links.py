#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:52:40 2020

@author: A.Baran Ertemir
"""

import argparse
import requests
from bs4 import BeautifulSoup
import time
import os

RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
ORANGE='\033[0;33m'
LIGHTBLUE='\033[1;34m'
LIGHTGREEN='\033[1;32m'

ap = argparse.ArgumentParser()

ap.add_argument("--url","-u", help="Please enter a URL.", required='True')

args = vars(ap.parse_args())

header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; rv:20.0) Gecko/20121202 Firefox/20.0"}
request = args['url']
response = requests.get(request,headers=header)
html = response.content
soup = BeautifulSoup(html,"html.parser")


print(f'{BLUE}Please wait while system is Loading...{NC}')
time.sleep(0.75)
os.system('clear')
print(f'{LIGHTGREEN}-----------------------------------ALL LINKS-----------------------------------{NC}')

print(f"{CYAN}<a> tags:{NC}")
for i in soup.find_all("a"):
        print(i.get('href'))
print("-------------------------------------------------------------------------------")

print(f"{YELLOW}<img> tags:{NC}")
for i in soup.find_all("img"):
    if "None" != i:
        print(i.get('src'))
print("-------------------------------------------------------------------------------")

print(f"{GREEN}<link> tags:{NC}")
for i in soup.find_all("link"):
    if "None" != i:
        print(i.get('href'))
print("-------------------------------------------------------------------------------")

print(f"{ORANGE}<script> tags:{NC}")
for i in soup.find_all("script"):
    try:
        print(i.get('src').replace("None",""))
    except:
        pass
print("-------------------------------------------------------------------------------")

print(f"{LIGHTBLUE}<audio> tags:{NC}")
for i in soup.find_all("audio"):
    if "None" != i:
        print(i.get('src'))
print("-------------------------------------------------------------------------------")