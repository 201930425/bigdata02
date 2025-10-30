import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wh = pd.read_csv('wh.csv')
# print(wh.head())
print(wh.describe())
# print(wh.info())
sns.scatterplot(x='Weight', y='Height', data=wh)
plt.show()