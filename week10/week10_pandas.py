import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

german = pd.read_csv('german.csv')
ages = [10,20,30,40,50,60,70,80]
print(pd.cut(german['Age'],bins=ages,right=False).reset_index().groupby('Age').count())
