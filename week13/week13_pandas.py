import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

apple = pd.read_csv('APPL_price.csv')
# print(apple.head())
# print(apple.describe())
# print(apple.info())
apple['Date'] = pd.to_datetime(apple['Date'])
# print(apple.info())
apple = apple.set_index('Date') # index를 날짜 시간컬럼으로 대체
# print(apple.head())
# print(apple.tail())

#시계열 데이터 슬라이싱
# print(apple['2022-06-14':'2022-06-16'])
# print(apple['2022-04':'2022-06'])

print(apple['Close'])
apple1m = apple.resample('1m').mean() #일주일 단위로 행을 묶어 평균값 추출
print(apple1m['Close'])
# print(apple7days.info())
# print(apple7days.describe())