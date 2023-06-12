# данные рост - вес, вес расчитывается по индексу массы тела (ИМТ)
import numpy as np
import pandas as pd
noise = 0.1
countRec = 100
for j in range(3):
    height = np.random.normal(175, 15 + noise * j, countRec)
    weight = []
    for i in height:
        weight.append(np.random.normal(23.5, 7.5 + noise * j ,1)[0] * i * i / 10000)
    data = pd.DataFrame(data = [height,weight],index = ['height','weight']).transpose()
    data[0: int(countRec * 0.8)].to_csv("train/" + "data sample #" + str(j) + ".csv")
    data[int(countRec * 0.8): countRec].to_csv("test/" + "data sample #" + str(j) + ".csv")
