#가상화폐 티커 목록 얻기

import pybithumb

tickers = pybithumb.get_tickers()
print(tickers)
print(len(tickers))     #bithumb에서 몇개의 코인이 거래되는지 갯수 확인