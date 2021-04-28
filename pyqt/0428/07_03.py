import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5    #해당 요일의 (최고가 - 최저가) 를 range 라는 컬럼을 만들어서 추가해줌.
df.to_excel("btc2.xlsx")