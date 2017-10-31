# -*- coding: utf-8 -*-
import json
import urllib2

btc_json = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR')
btc_obj = json.load(btc_json)
btcRate = btc_obj[0]["price_eur"]

bch_json = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/?convert=EUR')
bch_obj = json.load(bch_json)
bchRate = bch_obj[0]["price_eur"]

btcBeforeBCC = []
btcAfterBCC = []
btcAfterSegwit2x = []

print('BTC:')
for coin in btcAfterBCC:
    print(str(float(btcRate)*coin)+' €')
print('BCC:')
for coin in btcBeforeBCC:
    print(str(float(bchRate)*coin)+' €')
