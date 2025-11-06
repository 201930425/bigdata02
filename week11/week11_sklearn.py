import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes, load_breast_cancer

cancer = load_breast_cancer()
# print(cancer)
# print(cancer.target)
df_cancer = pd.DataFrame(cancer.data,columns=cancer.feature_names)
df_cancer['target'] = cancer.target
# print(df_cancer.info())

plt.figure(figsize = (10,6))
sns.boxplot(x='target',y='mean radius',data=df_cancer)
plt.xlabel('Target')
plt.ylabel('Mean radius')
plt.title('Mean radius of diabetes(0: Malignant , 1: Benign)')
plt.show()
