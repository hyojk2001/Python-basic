import pyupbit

orderbook = pyupbit.get_orderbook("KRW-BTC")
# get_orderbook()함수를 통해 10호가 데이터를 얻을 수 있다
# 리스트 안에 딕셔너리 데이터가 들어있는 형태
bids_asks = orderbook[0]['orderbook_units']

for bid_ask in bids_asks:
    print(bid_ask)