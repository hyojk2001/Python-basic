#DataFrame 생성 - 가로축/세로축(열 + 열이름)이 있는 2차원 데이터를 저장하는 자료구조
from pandas import DataFrame

data = {'open':[100,200], 'high':[110,210]}
df = DataFrame(data)
print(df) 