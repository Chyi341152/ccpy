#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import sys
from ccpy.ccpy.ccpy import print_help, conversion, countries


def rewrite_README():
    """Write README to current folder"""
    MD = '''
# ccpy (Currency Converter Python) 

A ccpy project that exists as an aid to the Convert one currency to another.

## Installation

ccpy works on macOS, GNU/Linux, and Windows, with binary downloads available for [every release.](https://github.com/chyi341152/ccpy/release) You can also install it with pip.

`$ pip install ccpy`

or apt-get if you're using Linux:

`$ sudo apt-get install ccpy`

Requires Python 3.0 or higher.

## Usage

Usage: __from ccpy import ccpy; print(ccpy.conversion(f="USD",t="CNY"))__

Return: __{USD_CNY}__ 

-- ccpy.conversion(f="USD",t="CNY") get Exchange Rate from United States Dollar to Chinese Yuan

Exchange Rate time : {datetime}

ccpy[🍰 🐜 🍰], 0.0.1 - Made by @Chyi's
-- Currency Converter Python

List of All Countries

| # | ID | CurrencyName | CurrencySymbol|
|:---:|:---:|:---:|:---:| '''.format(USD_CNY=conversion(f="USD",t="CNY"),
                                     datetime=datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    MD += '\n'
    indexNum = 0
    for key, value in countries().items():
        indexNum += 1
        MD += '|{num}|{ID}|{CurrencyName}|{CurrencySymbol}|\n'.format(num=indexNum,ID=key, CurrencyName=value["currencyName"], CurrencySymbol=value.get("currencySymbol","\U0001F914"))

    MD += '''

## Contributing

To make a contribution. fork the repo. make you change and then submit a pull request. Please try to adhere to the existing style. If you've discovered a bug
or have a feature requests, create an [issue](https://github.com/chyi341152/ccpy/issues/new) and I'll take care of it!

__Pending Feature__
* Support Local History search

## Technologies

ccpy is written in Python and built on Free Currency Converter API.

## Acknowledgements

    '''
    with open('../README.md','w') as f:
        f.write(MD)


def run():
    rewrite_README()
    print('ccpy finish write README.md')


if __name__ == "__main__":
    run()