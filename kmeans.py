import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

usa = pd.read_csv(r"DB\United States 10-Year Bond Yield.csv")

PriceUSA = usa['Price']
ChangeUSA = usa['Change %']
HighUSA = usa['High']
LowUsa = usa['Low']
OpenUsa = usa['Open']
# create dataset

# plot
plt.scatter(
   PriceUSA, ChangeUSA,
   c='white', marker='o',
   edgecolor='black', s=50
)
plt.show()

from sklearn.cluster import KMeans

km = KMeans(
    n_clusters=3, init='random',
    n_init=10, max_iter=300, 
    tol=1e-04, random_state=0
)
