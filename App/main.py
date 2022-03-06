import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def call_api(type="latest",symbol=None):
	if type == "latest":
		url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
		parameters = {
			'start':'1',
			'limit':'100',
			'convert':'USD'
		}
	elif type=="info":
		url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
		parameters = {
			'symbol':symbol
			}

	headers = {
	'Accepts': 'application/json',
	'Accept-Encoding': 'deflate, gzip',
	'X-CMC_PRO_API_KEY': '70d8299f-0b97-41f8-96e3-f56fb66df902',
	}
	session = Session()
	session.headers.update(headers)

	try:
		response = session.get(url, params=parameters)
		data = json.loads(response.text)
		return data
	except (ConnectionError, Timeout, TooManyRedirects) as e:
		print(e)



from flask import Flask, render_template, request

def filter_data(symbol, data):
	filtered = [i for i in data if i["symbol"]==symbol]
	if len(filtered)>0:
		filtered = filtered[0]
		return filtered

	else:
		return 'price not found'

def coin_dictionary(sym, dict_data, data_listings):
	data = call_api(type = 'info', symbol = sym)
	coin_data_listings = filter_data(sym, data_listings)
	if "data" in data.keys():
		data = data["data"]
		dict_data['precio'] = coin_data_listings['quote']['USD']['price']
		dict_data['logo']=data[sym]['logo']
		dict_data['slug'] =  data[sym]['slug']
		dict_data['descripcion'] = data[sym]['description']
		dict_data['source_code'] = data[sym]["urls"]['source_code'][-1]
		dict_data['website'] = data[sym]['urls']['website'][-1]
		return dict_data
	else:
		return 'API error'

app = Flask(__name__)
@app.route('/')

def html():
	#Consume coinmarketcap API
	data = call_api()
	if "data" in data.keys():
		data = data["data"]
		data2 = data[0:10]

	else:
		return "Failed to load data"

	dict_btc = {}
	dict_btc = coin_dictionary(sym = "BTC", dict_data = dict_btc, data_listings= data)

	dict_eth = {}
	dict_eth = coin_dictionary(sym ="ETH", dict_data = dict_eth, data_listings = data)
	 
	return render_template('index.html',coins = data2, btc=dict_btc, eth = dict_eth)
	

if __name__ == '__main__':
    app.run()
