import pybithumb

df = pybithumb.get_ohlcv("BTC")
print(df)
yesterday = df.iloc[-2]                 #끝에서 2번째 행(=전일 데이터)를 ㅡ가져온다

today_open = yesterday['close']         #어제의 종가 = 오늘의 시가
yesterday_high = yesterday['high']      #전일 고가
yesterday_low = yesterday['low']        #전일 저가
target = today_open + (yesterday_high - yesterday_low) * 0.5    # 변동성 돌파전략의 목표가 계산(당일 시가 + 레인지(고가-저가) * 0.5)
print(target)