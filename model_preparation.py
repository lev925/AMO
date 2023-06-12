import pandas as pd
from sklearn.linear_model import LinearRegression
df_train = pd.read_csv("train/data sample #0.csv", index_col = 0)
df_test = pd.read_csv("test/data sample #0.csv", index_col = 0)
model = LinearRegression()
model.fit(df_train['height'].values.reshape(-1,1), df_train['weight'])
pred = model.predict(df_test['height'].values.reshape(-1, 1))
pd.DataFrame(data = [df_test["height"].values, pred], index=['height','weight']).transpose().to_csv("test/data_predict#0.csv")