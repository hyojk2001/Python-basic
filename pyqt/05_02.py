#현 시각 비트코인/이더리움 가격 알아보기

import pybithumb

price = pybithumb.get_current_price("BTC")
price2 = pybithumb.get_current_price("ETH")
print(price)
print(price2)