import datetime

dt = datetime.datetime(2018,12,1)
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
#timedelta(1) : 1일의 시간을 의미한다
print(now)
print(mid)