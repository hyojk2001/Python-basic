import pybithumb

orderbook = pybithumb.get_orderbook("BTC")      #비트코인의 호가정보
# print(orderbook)

# for k in orderbook:
#     print(k)

bids = orderbook['bids']
# print(bids)

for bid in bids:
    print(bid)
    
# asks = orderbook['asks']
# print(asks)
