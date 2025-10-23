import pandas as pd

uber = pd.read_csv("uber.csv")
# print(type(uber))
# print(uber.head(7))
# print(uber.info())
# print(uber.describe())

# print(uber[uber['MILES*'] == 12204.7])
# print(uber[uber["MILES*"] == uber["MILES*"].max()])
print(uber.tail())
uber.drop(1155,inplace=True)
print(uber.tail())
print(uber.describe())