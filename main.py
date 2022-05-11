"""
    ANALITICS MAIN
"""
import pandas as pd
import numpy as np

usa = pd.read_csv(r"DB\United States 10-Year Bond Yield.csv")

# United States
# print(usa) # Here we simply print the csv
# print(usa.head(6)) # Here we take the very first 5 rows of data

# Dataframes de el precio asi como el cambio
PrecioUSA = usa['Price'] # Dataframe for the price
CambioUSA = usa['Change %'] # Dataframe for the Change in percentage
print(PrecioUSA)

# Some statistics stuff
#AvPrecio = np.average(PrecioUSA)
# AvCambio = CambioUSA.mean()

# Here we print the statistics stuff
#print("Average of prices: ",AvPrecio)
# print("Average of change: ",AvCambio)