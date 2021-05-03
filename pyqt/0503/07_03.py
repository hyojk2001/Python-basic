# 레인지 : 전일 고가에서 저가를 뺀 값. 백테스팅 시 모든 거래일을 기준으로 레인지를 계산해야 함.
import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df.to_excel("btc.xlsx")