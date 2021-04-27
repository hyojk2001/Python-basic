import pyupbit

tickers = pyupbit.get_tickers()
print(tickers)

for i in tickers:
    if 'KRW' in i:
        print(i)

# price = pyupbit.get_current_price("KRW-BTC")
# print("현재 비트코인의 가격 : " , price, "입니다")

# price = pyupbit.get_current_price(["KRW-BTC","KRW-XRP"])
# print(price)