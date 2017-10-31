import json
import urllib2

j = urllib2.urlopen('https://api.coindesk.com/v1/bpi/currentprice.json')
j_obj = json.load(j)
bpi = j_obj["bpi"]
eur = bpi["EUR"]
eurRate = eur["rate"].replace(',','')

myCoins = [YOUR NUMBER OF BTC]

print(float(eurRate)*myCoins)
