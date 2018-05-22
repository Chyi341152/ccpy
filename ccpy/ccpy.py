#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import random
import sys

from . __version__ import (__title__,__description__,__url__,__version__,__build__,__author__,__author_email__,__license__,__copyright__,__mascot__)

BASE_URL = "https://free.currencyconverterapi.com/api/v5"

# ASCII color codes
GREEN       = '\033[92m'
GRAY        = '\033[90m'
CYAN        = '\033[36m'
RED         = '\033[31m'
YELLOW      = '\033[33m'
END         = '\033[0m'
UNDERLINE   = '\033[4m'
BOLD        = '\033[1m'

USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Firefox/59",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
]

# list of countries
def countries():
    api_url = BASE_URL + "/currencies"
    resp = requests.get(api_url, headers={"user-agent":random.choice(USER_AGENTS)})
    assert resp.status_code == 200
    respJson = resp.json()
    # ex. "CNY":{"currencyName":"Chinese Yuan","currencySymbol":"¥","id":"CNY"}
    return respJson["results"]

# Check now currency Converter
def conversion(f="USD",t="CNY"):
    if f in countries().keys() and t in countries().keys():
        api_url = BASE_URL + "/convert?q={}_{}&compact=y".format(f,t)
    else:
        print('{},{} 无效'.format(f,t))
        return False
    resp = requests.get(api_url, headers={"user-agent": random.choice(USER_AGENTS)})
    assert resp.status_code == 200
    respJson = resp.json()
    return respJson["{}_{}".format(f,t)]["val"]

# Helper Functions
def print_help():
    """ Prints usage instructions """
    """Prints usage instructions."""
    sys.stdout.write("{}{}[{}], {} - Made by @{}{}\n".format(CYAN,__title__,__mascot__,__version__,__author__,END))
    sys.stdout.write("-- Currency Converter Python")

    sys.stdout.write("\n\n{}List of All Countries{}".format(RED, END))
    for key, value in countries().items():
        sys.stdout.write("""\n{}"ID"={}, "CurrencyName"={:^50}, "CurrencySymbol"={}{}""".format(GREEN,key,value["currencyName"],value.get("currencySymbol","Unknown"),END))

    sys.stdout.write("""\n\n{}Usage:{} import ccpy; {}print(ccpy.conversion(f="USD",t="CNY")){} \n{}Return: {}{}\n""".format(UNDERLINE, END, YELLOW, END, GREEN,conversion(f="USD",t="CNY"),END))


if __name__ == "__main__":
    print_help()