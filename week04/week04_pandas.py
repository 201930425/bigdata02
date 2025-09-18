from operator import index

import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset('mpg')
#
# mpg_nan = mpg[mpg['horsepower'].isnull()]
# print(mpg_nan[['mpg','horsepower','displacement', 'origin']])

# 결측치 처리 #1
mpg.dropna(inplace=True) # mpg = mpg.dropna()
print(mpg.info())
# print(mpg[mpg['horsepower'].isnull()])

# 결측치 처리 #2
# mpg = mpg.fillna(mpg['horsepower'].mean())
# print(mpg[mpg['horsepower'].isnull()])
# print(mpg.info())