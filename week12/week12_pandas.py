import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wh = pd.read_csv('wh.csv')
# print(wh.head())
# print(wh.describe())
# print(wh.info())
# 파운드 ( 1 == 453.592g), 인치 (1 == 2.54cm
# print(wh.query('Weight > 350'))
print(wh[wh['Weight']>=390])
# sns.scatterplot(x='Weight', y='Height', data=wh)
# plt.show()