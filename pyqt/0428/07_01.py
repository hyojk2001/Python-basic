# 백테스팅 : 과거의 정보를 통해 투자 전략이 어느 정도의 효율을 지니는지 확인하는 작업
import pybithumb

df = pybithumb.get_ohlcv("BTC")
df.to_excel("btc.xlsx")
print(df)