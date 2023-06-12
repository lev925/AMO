import pandas as pd
data = pd.read_csv("train/data sample #0.csv", index_col=0)
data = data[data['height'] < 210]
data = data[data['height'] > 140]
data.to_csv("train/data sample #0.csv")