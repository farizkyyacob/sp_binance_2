import ccxt
import config
import time
from threading import *


exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': config.api_key(),
    'secret': config.api_secret(),
    'options': {
        'defaultType': 'future', },
})


x = exchange.fetch_balance(params={'type': 'future'})
first_order = x["info"]['totalWalletBalance']
print(first_order)