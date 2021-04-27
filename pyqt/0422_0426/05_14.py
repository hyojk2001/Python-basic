#거래소 과거 시세 얻어오기

import pybithumb

btc = pybithumb.get_ohlcv("BTC")
print(btc)