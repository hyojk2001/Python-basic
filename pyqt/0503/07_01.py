import pybithumb

df = pybithumb.get_ohlcv("BTC")
df.to_excel("btc.xlsx")
print(df.tail())
print(df.tail(10))