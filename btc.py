# -*- coding: utf-8 -*-
import json
import requests

def checkBalance(addr):
	sat_url = 'https://blockchain.info/q/addressbalance/' + addr
	satoshi = float(requests.get(sat_url).content)
	bitcoin = satoshi / 100000000
	return bitcoin

def bitcoinToFIAT(btc, rate):
	if btc is None: return 0
	return round(float(rate) * btc, 3)

def main():
	btc_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR'
	btc_json = requests.get(btc_url)
	btc_obj = btc_json.json()[0]
	btcEUR = btc_obj['price_eur']
	btcUSD = btc_obj['price_usd']

	addresses = []

	totalBTC = 0
	totalEuros = 0
	totalDollars = 0

	for address in addresses:
		bitcoin = checkBalance(address)
		euros 	= bitcoinToFIAT(bitcoin, btcEUR)
		dollars = bitcoinToFIAT(bitcoin, btcUSD)
		totalBTC		+= bitcoin
		totalEuros		+= euros
		totalDollars	+= dollars
		if bitcoin!=0: print(str(bitcoin) + ' BTC | ' + str(euros) + ' € | ' + str(dollars) + ' $')

	print('\n-----------------------------------------------')
	print(str(totalBTC) + ' BTC | ' + str(totalEuros) + ' € | ' + str(totalDollars) + ' $')
	print('BTC: ' + str(btcEUR) + ' €')
	print('BTC: ' + btcUSD + ' $')

main()