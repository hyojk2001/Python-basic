import pybithumb

con_key = "224a47977687bb70eca884f164c3f79a"
sec_key = "b845dc01063e3038e277008af88b4f78"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 06_05
# order = bithumb.buy_limit_order("BTC",4000100,0.001)
# print(order)

# 06_07
# krw = bithumb.get_balance("BTC")[2]
# orderbook = pybithumb.get_orderbook("BTC")

# asks = orderbook['asks']
# sell_price = asks[0]['price']
# unit = krw/sell_price
# print(unit)

# 06_08
order = bithumb.buy_limit_order("BTC",40000000,1)
print(order)