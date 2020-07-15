import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode

df=pd.read_csv('HamoyeData1.csv')
#print(df.head(10))

#getting the modal class in fuel_unit
print(df.fuel_unit)
modalfuelunit=mode(df.fuel_unit).mode[0]

print(modalfuelunit)

#replacing missing values in fuel_unit and assigning the new variable to it

#df.fuel_unit=df.fuel_unit.fillna(modalfuelunit)
#missingfuelunit=df.fuel_unit.isnull().sum()
#print(missingfuelunit)


#checking the cprrelation between all numerical values (int and float)
numfeatures=df.select_dtypes(include=['int', 'float'])
numfeatures
numfeaturescor=numfeatures.corr()['fuel_cost_per_unit_burned'][:]

corels=(numfeaturescor[abs(numfeaturescor) > 0.0]).sort_values(ascending=False)
print(corels)

print(df.describe()) #to see the 75th percentile and standard deviation
#checking for kurtosis and skewness
from scipy.stats import kurtosis, skew
print(kurtosis(df.fuel_qty_burned))
print(skew(df.fuel_qty_burned))

#checking the info to see missing patterns
print(df.info())
# checking for features with missing values
missing=df.isnull().sum()
print(missing)

#calculating total missing values and percentage in column with mising values 
totalmissingfuel_unit=df.fuel_unit.isnull().sum()
totalrows=len(df)
percmissing=(totalmissingfuel_unit/totalrows)*100
print("Percentage missing in fuel unit is {}%".format(percmissing.round(3)))


#Fuel type most burned viewed on a bar graph
plt.xlabel("Fuel type")
plt.ylabel("Fuel cost per unit burned")
plt.bar(df.fuel_type_code_pudl, df.fuel_cost_per_unit_burned)

# locating fuel cost per unit delivered for each year
# I didn't quite get the question because of my network, but I wrote some codes for its execution below
# Function to calculate unit cost delivered for each year:
# This function takes two keyword arguments; dataframe and year 
def PercentCostDelivered(dataframe, year):
	costunitdelivered=dataframe.iloc[year]
	totalcostunitdelivered=dataframe.sum()
	percentdeliveredyear=((costunitdelivered/totalcostunitdelivered)*100).round(5)
	percentyear=("percentage cost unit delivered for the chosen year is {}%"\
		.format(percentdeliveredyear))
	return percentyear
	
print(PercentCostDelivered(df.fuel_cost_per_unit_delivered, 2018))











#df.boxplot(column='fuel_cost_per_unit_burned', by='fuel_unit')