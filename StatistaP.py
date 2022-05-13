import pandas as pd
import numpy as np
import statistics as stat
import statsmodels.api as sm 

usa = pd.read_csv(r"DB\United States 10-Year Bond Yield.csv")
cseven = pd.read_excel(r"DB\7anios.xlsx")
csix = pd.read_excel(r"DB\6anios.xlsx")
cfive = pd.read_excel(r"DB\5anios.xlsx")
    # United States
    #print(usa) # Here we simply print the csv
    #print(usa.head(6)) # Here we take the very first 5 rows of data

    # Dataframe
PriceUSA = usa['Price'] # Dataframe for the price
ChangeUSA = usa['Change %'] # Dataframe for the Change in percentage
DatesUSA = usa['Date']

PriceOF = cfive['Price']
ChangeOF = cfive['Change %']
DatesOF = cfive['Date']

PriceSIX = csix['Price']

# Some statistics stuff
# Change
AvChange = ChangeUSA.mean()
MAXChange = np.max(ChangeUSA)
MINChange = np.min(ChangeUSA)
RanChange = MAXChange-MINChange
VarChange = stat.variance(ChangeUSA)
ModChange = stat.mode(ChangeUSA)
SUMChange = np.sum(ChangeUSA)
(unique, counts) = np.unique(ChangeUSA, return_counts=True)
Changefrequencies = np.asarray((unique, counts)).T

X = usa[["Low","High"]]
y = usa["Price"]
X = sm.add_constant(X)   # se agrega la intercepción, la ordenada al origen (beta_0) el modelo

modelo = sm.OLS(y, X).fit()

predictions = modelo.predict(X)  # Con el modelo, se calculan las Y´s
print("_______________________________________-")
print(modelo.summary())
    # Price
AvPrice = np.average(PriceUSA)
MAXPrice = np.max(PriceUSA)
MINPrice = np.min(PriceUSA)
RanPrice = MAXPrice-MINPrice
VarPrice = stat.variance(PriceUSA)
ModPrice = stat.mode(PriceUSA)
SUMPrice = np.sum(PriceUSA)

# Here we print the statistics stuff
print(" ")
print("STATISTICS:") # Simply a title
print("___________________________________________________ ")
print(" ")
print("COLUMN PRICE: ")
print(" ")
print("Average of prices: ",AvPrice)
print("Max value of the price column: ",MAXPrice)
print("Min value of the price column: ",MINPrice)
print("Range of the price column: ",RanPrice)
print("Variance of the price column: ",VarPrice)
print("Mode of the price column: ",ModPrice)
print("SUM of the price column: ",SUMPrice)
print("___________________________________________________")
print("COLUMN CHANGE: ")
print(" ")
print("Average of change: ",AvChange)
print("Max value of the change column: ",MAXChange)
print("Min value of the change column",MINChange)
print("Range of the change column:",RanChange)
print("Variance of the change column: ",VarChange)
print("Mode of the change column: ",ModChange)
print("SUM of the change column: ",SUMChange)
print(" ")
print("Change frequency : ",Changefrequencies)



