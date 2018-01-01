# -*- coding: utf-8 -*-
import json
import urllib2

btc_json = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR')
btc_obj = json.load(btc_json)
btcRate = btc_obj[0]["price_eur"]

bch_json = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/?convert=EUR')
bch_obj = json.load(bch_json)
bchRate = bch_obj[0]["price_eur"]

# fill in balances from exchanges in BTC directly here
exchanges = []

# put btc & bch addresses here
addresses = []

totalEuros = 0

print('Balances:')
for address in addresses:
	btc_balance_json = urllib2.urlopen('https://blockchain.info/q/addressbalance/'+address)
	bch_balance_json = urllib2.urlopen('https://blockdozer.com/insight-api/addr/'+address+'/totalReceived')

	for b in [btc_balance_json, bch_balance_json]:
		balance_sat = float(json.load(b))
		balance = balance_sat / 100000000
		euros = round(float(btcRate if b == btc_balance_json else bchRate) * balance, 3)
		if euros == 0: continue
		totalEuros += euros
		print(str(euros) + ' € '+' in '+('BTC' if b == btc_balance_json else 'BCH'))

for exchange in exchanges:
	euros = round(float(btcRate) * exchange, 3)
	totalEuros += euros
	print(str(euros) + ' € on exchange')

print('')
print('Total:')
print(str(totalEuros)+' €')
print('')

