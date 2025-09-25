import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsRegressor
import tglearn as tg

df = pd.read_csv('lifesat_satisfaction.csv')
X = df[["GDP per capita (USD)"]].values
y = df[["Life satisfaction"]].values

# model1 = LinearRegression()
# model2 = KNeighborsRegressor(3)
model1 = tg.LinearRegression()
model2 = tg.KNeighborsRegressor(n_neighbors=5)

model1.fit(X, y)
model2.fit(X, y)

new_instance = [[31_721.30]] #SouthKorea GDP per capita (usd) 2020
print(f"Life satisfaction (Linear Regression) : {model1.predict(new_instance)[0][0]:.1f}")
print(f"Life satisfaction (KNeighbors Regression) : {model2.predict(new_instance)[0][0]:.1f}")
