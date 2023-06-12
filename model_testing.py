import pandas as pd
from sklearn.metrics import mean_squared_error
test = pd.read_csv("test/data sample #0.csv", index_col = 0)
predict = pd.read_csv("test/data_predict#0.csv", index_col = 0)
mse = mean_squared_error(test["weight"],predict["weight"],squared=False)
print(mse)