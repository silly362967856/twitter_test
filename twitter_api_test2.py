# -*- coding:utf-8 -*-

from TwitterAPI import TwitterAPI

api = TwitterAPI(consumer_key='gfTbGBbYDaR30QzbsTT7gR2W8',consumer_secret='UivvLGy6sYoXdPklcpzkGVG5vceBNXYfW7TmMkv5iIaB0y6bAH',access_token_key='847624545448022018-IyAAKO3kk4JVuhhlhe0L6ofiY2vt2u7',access_token_secret='aNH8krGomaRhJKv2ManYlyby9gvejgAZy91giHjscbcMw')

r = api.request('statuses/filter',{'track':'coupon'})
for item in r:
	print(item)
