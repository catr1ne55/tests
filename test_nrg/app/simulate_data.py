import numpy as np
import pandas as pd

columns = [i for i in range(365)]

price = initial_price = 100
rows = []
for r in range(1000):
    prices = []
    for i in range(365):
        price *= (1 + np.random.normal(loc=0.0001, scale=0.005))
        prices.append(price)
    rows.append(prices)


df = pd.DataFrame(rows, columns=columns)
df = df.rename_axis('id').reset_index()
df.to_csv('dataset.csv')
