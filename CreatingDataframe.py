import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read with headers
df=pd.read_csv("NEO Earth Close Approaches (2).csv", )

print(df)

# Get the total number of rows
rowCount = df.shape[0]
print('Total rows are ')
print(rowCount)

# Get the total number of columns
columnCount = df.shape[1]
print('Total columns are ')
print(columnCount)

#Get the mean of the The minimum possible close-approach distance
print('The mean of the minimum possible close-approach distance (Earth center to NEO center), in kilometers is')
print(df['CA DistanceMinimum (km)'].mean())

#Get the maximum value of the The minimum possible close-approach distance
print('The maximum value of the minimum possible close-approach distance (Earth center to NEO center), in kilometers in this list is')
print(df['CA DistanceMinimum (km)'].max())

#Get the minimum value of the The minimum possible close-approach distance
print('The minimum value of the minimum possible close-approach distance (Earth center to NEO center), in kilometers in this list is')
print(df['CA DistanceMinimum (km)'].min())

# Creating a table with Dataframe

##define figure and axes
fig, ax = plt.subplots()

##hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

##create Dataframe
data = pd.read_csv("NEO Earth Close Approaches (2).csv", nrows=10, usecols=["Object","CA DistanceMinimum (km)", "Diameter"])
df = pd.DataFrame(data)

## Create table
table = ax.table(cellText=df.values, colLabels=df.columns, colColours =["palegreen"] * 10, cellLoc ='center', loc='center')

##display table
fig.tight_layout()
plt.show()