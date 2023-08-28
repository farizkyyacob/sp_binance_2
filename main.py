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
wallet_balance = x["info"]
floating_info = x["info"]
futures_wallet = x["info"]
print("wallet_balance : ",wallet_balance)
print("Floating Info : ",floating_info)
print("Futures Wallet Info : ", futures_wallet)


#x = exchange.publicGetExchangeInfo()
#x =exchange.markets["LTC/USDT"]
#print(x)
#for a in x:
#    print(a)