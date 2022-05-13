import pandas as pd
import numpy as np
import statistics as stat

usa = pd.read_csv(r"DB\United States 10-Year Bond Yield.csv")
    # United States
    #print(usa) # Here we simply print the csv
    #print(usa.head(6)) # Here we take the very first 5 rows of data

    # Dataframe
PriceUSA = usa['Price'] # Dataframe for the price
ChangeUSA = usa['Change %'] # Dataframe for the Change in percentage
DatesUSA = usa['Date']
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
print("Change frequency : ",Changefrequencies)
print(" ")


