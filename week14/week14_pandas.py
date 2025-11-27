import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pr = pd.read_csv('product.csv')
# print(pr.info())
# print(pr.describe())
# print(pr.tail())
# print(pr.head())
# print(pr['operator'].unique())
# print(pr['process'].unique())
# print(pr['factory'].unique())
pr['path'] = pr.groupby('product_id')['operator'].transform(
    lambda x: '_'.join(x)
)
# print(pr.head())
pr['path'] = pr['factory'] + '_' + pr['path']
# print(pr.head())
pr = pr.drop_duplicates('product_id')
# print(pr)
pr = pr[['date','product_id','passfail','path']]
# print(pr)
print(pr.groupby('passfail')['path'].value_counts())