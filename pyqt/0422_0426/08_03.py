import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", interval = "minute", count = 5)
# get_ohlcv : 가상화폐의 티커를 입력받아 OHLCV 데이터를 판다스 DataFrame으로 반환.
# DataFrame에 바인딩 된 값을 출력한 결과
# interval 옵션으로 월/주/일/분봉 중 하나를 선택 가능.
# count 로 가장 최근부터 몇개를 뽑을 건지 선택 가능
print(df)