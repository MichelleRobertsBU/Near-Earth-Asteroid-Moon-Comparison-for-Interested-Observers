
import colorsys
from xml.dom.minidom import DocumentType
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

#Downloaded CSV file on Near Earth Asteroid tracking to analyze the data in comparison
to the Earth's Moon for interested observers. The data is from NASA public domain. See 
the README for License information and key for the column information.
##Requirement (1) Read in data from a local csv file with Pandas read_functions.

df = pd.read_csv('NEO_Earth_Close_Approaches.csv')
df.head()
print(df)

#Information on data type for each column
print(df.dtypes)

# Set figure size for graph
plt.rcParams["figure.figsize"] = [12.00, 6.50]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns needed for data analysis
columns = ['CA DistanceMinimum (km)','Object']
df = pd.read_csv('NEO_Earth_Close_Approaches.csv', usecols=columns)

# Scatter plot showing Near Earth Asteroids and Mininmum distance in kilometers.
##Requirement (4) Visualize your data. Make 2 basic plots with matplotlib.
colors = np.random.randint(43, size=(43))
df.plot.scatter(x = 'Object', y = 'CA DistanceMinimum (km)', c=colors, cmap='nipy_spectral')

#Add title and labels to x- and y-axis
plt.suptitle('The minimum possible close-approach distance (Earth center to NEO center), in kilometers', fontsize = 15)
plt.ylabel('Minimum Distance')
plt.xlabel('Near Earth Object')
plt.xlim(left=-1, right=43)
#rotate x-axis tick labels
plt.xticks(rotation=90) 
plt.show()

#Create 2 Diameter Columns to illustrate the variation in estimated diameter of each asteroid.
##Requirement (2) Manipulate and clean data.
df2 = pd.read_csv("NEO_Earth_Close_Approaches.csv")
df2[['Min Diameter','Max Diameter']] = df2["Diameter"].str.split("-", expand=True)
print("\n After adding two new columns : \n", df2)

#read with headers
df=pd.read_csv("NEO_Earth_Close_Approaches.csv")
print(df)

#The following numpy functions were used to find out the number of rows, number of columns, mean, 
standard deviation, maximum and minimum values of the close-approach distance.
##Requirement (3) Do 5 basic calculations with Pandas or use 5 different built-in Python functions
to find out something about your data. 

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

#Get the standard deviation of The minimum possible close-approach distance
print('The standard deviation of the minimum possible close-approach distance (Earth center to NEO center), in kilometers is')
print(df['CA DistanceMinimum (km)'].std())

#Get the maximum value of the The minimum possible close-approach distance
print('The maximum value of the minimum possible close-approach distance (Earth center to NEO center), in kilometers in this list is')
print(df['CA DistanceMinimum (km)'].max())

#Get the minimum value of the The minimum possible close-approach distance
print('The minimum value of the minimum possible close-approach distance (Earth center to NEO center), in kilometers in this list is')
print(df['CA DistanceMinimum (km)'].min())

# Creating a table with Dataframe

##define figure and axes
fig, ax = plt.subplots()
plt.suptitle('Ten closest Asteroids (Earth center to NEO center), with Minimum Distance in kilometers and Diameter in meters', fontsize = 15)

##hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

##create Dataframe
data = pd.read_csv("NEO_Earth_Close_Approaches.csv", usecols=["Object","CA DistanceMinimum (km)", "Diameter"])
df = pd.DataFrame(data.tail(10))

## Create table
table = ax.table(cellText=df.values, colLabels=df.columns, colColours =["palegreen"] * 10, cellLoc ='center', loc='center')
table.set_fontsize(12)
table.scale(1,2)

##display table
fig.tight_layout()
plt.show()


#Pie chart of moon distance
##Requirement (4) Visualize your data. Make 2 basic plots with matplotlib.
fig1, ax1 = plt.subplots()
plt.title('Ten closest Asteroids', fontsize = 15)
plt.suptitle('The minimum possible close-approach distance in kilometers in comparison to the Moon distance.', fontsize = 15)
ax1.axis('equal')
plt.pie(df['CA DistanceMinimum (km)'], labels = df['Object'],textprops={"fontsize":10})
plt.show()

#Moon diameter comparison
##define figure and axes
fig, ax = plt.subplots()
plt.suptitle('Percent comparison to the Moon diameter of the ten closest Asteroids.', fontsize=15)

##hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

df3 = pd.read_csv("NEO_Earth_Diameter.csv", usecols = ["Object", "Min Diameter"])
df3.head()
*Calculate the percent diameter compared to the Moon.
##Requirement (2) Manipulate and clean data.
df3['Min Diameter']= df3['Min Diameter'].div(3474000)*(100)
df3 = pd.DataFrame(df3.tail(10))

## Create table
table = ax.table(cellText=df3.values, colLabels=df3.columns, colColours =["palegreen"] * 10, cellLoc ='center', loc='center')
table.set_fontsize(12)
table.scale(1,2)

##display table
fig.tight_layout()
plt.show()

#Bar chart of diameter comparison
##Requirement (4) Visualize your data. Make 2 basic plots with matplotlib.
df3 = df3 = pd.read_csv("NEO_Earth_Diameter.csv")
plt.rcParams["figure.figsize"] = [14.00, 6.50]
plt.rcParams["figure.autolayout"] = True

df3.plot(y = "Min Diameter", x = "Object", kind='bar')
plt.suptitle('Near Earth Asteroids Minimum Diameter in meters')
plt.show()

#display image

im = img.imread('PIA25329_small.jpg')
plt.axis('off')
plt.imshow(im)

plt.suptitle("The DART spacecraft, which is about the size of a vending machine, crashed into Dimorphos at 14,000 mph. This crash affected the asteroid's orbit")
plt.figtext(0.5, 0.05, "Dart Mission - images-assets.nasa.gov/image/PIA25329/PIA25329~orig.jpg and NASA/Johns Hopkins APL/Steve Gribbe", ha="center", fontsize=12, bbox={"alpha":0.5, "pad":5})
plt.show()
