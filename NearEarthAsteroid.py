
import colorsys
from xml.dom.minidom import DocumentType
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

df = pd.read_csv('NEO Earth Close Approaches (2).csv')
df.head()
print(df)

print(df.dtypes)

# Set the figure size
plt.rcParams["figure.figsize"] = [12.00, 6.50]
plt.rcParams["figure.autolayout"] = True

# Make a list of columns
columns = ['CA DistanceMinimum (km)','Object']

# Read a CSV file
df = pd.read_csv('NEO Earth Close Approaches (2).csv', usecols=columns)

# Plot the lines
colors = np.random.randint(43, size=(43))
df.plot.scatter(x = 'Object', y = 'CA DistanceMinimum (km)', c=colors, cmap='nipy_spectral')

#Add title and labels to x- and y-axis
plt.suptitle('The minimum possible close-approach distance (Earth center to NEO center), in kilometers')
plt.ylabel('Minimum Distance')
plt.xlabel('Near Earth Object')
plt.xlim(1)
#rotate x-axis tick labels
plt.xticks(rotation=45)
  
plt.show()

#Create 2 Diameter Columns
df2 = pd.read_csv("NEO Earth Close Approaches (2).csv")
df2[['Min Diameter','Max Diameter']] = df2["Diameter"].str.split("-", expand=True)

print("\n After adding two new columns : \n", df2)

#read with headers
df=pd.read_csv("NEO Earth Close Approaches (2).csv")
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
plt.suptitle('Ten closest Asteroids (Earth center to NEO center), with Minimum Distance in kilometers and Diameter in meters')

##hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

##create Dataframe
data = pd.read_csv("NEO Earth Close Approaches (2).csv", usecols=["Object","CA DistanceMinimum (km)", "Diameter"])
df = pd.DataFrame(data.tail(10))

## Create table
table = ax.table(cellText=df.values, colLabels=df.columns, colColours =["palegreen"] * 10, cellLoc ='center', loc='center')

##display table
fig.tight_layout()
plt.show()


#Pie chart of moon distance

fig1, ax1 = plt.subplots()
plt.title('The minimum possible close-approach distance in kilometers in comparison to the Moon distance. Ten closest Asteroids.')
ax1.axis('equal')
plt.pie(df['CA DistanceMinimum (km)'], labels = df['Object'],textprops={"fontsize":15})
plt.show()

#Moon diameter comparison
##define figure and axes
fig, ax = plt.subplots()
plt.suptitle('Percent comparison to the Moon diameter of the ten closest Asteroids.')

##hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

df3 = pd.read_csv("NEO Earth Diameter.csv", usecols=["Object", "Min Diameter"])
df3.head()

df3['Min Diameter']= df3['Min Diameter'].div(3474000)*(100)
df3 = pd.DataFrame(df3.tail(10))

## Create table
table = ax.table(cellText=df3.values, colLabels=df3.columns, colColours =["palegreen"] * 10, cellLoc ='center', loc='center')

##display table
fig.tight_layout()
plt.show()

#Bar chart of diameter comparison
df3 = df3 = pd.read_csv("NEO Earth Diameter.csv")
plt.rcParams["figure.figsize"] = [14.00, 6.50]
plt.rcParams["figure.autolayout"] = True

df3.plot(y = "Min Diameter", x = "Object", kind='bar')
plt.suptitle('Near Earth Asteroids Minimum Diameter in meters')
plt.show()

#display image

img = mpimg.imread('PIA25329_small.jpg')
imgplot = plt.imshow(img)
plt.suptitle("The DART spacecraft, which is about the size of a vending machine, crashed into Dimorphos at 14,000 mph. This crash affected the asteroid's orbit")
plt.figtext(0.5, 0.01, "Dart Mission - images-assets.nasa.gov/image/PIA25329/PIA25329~orig.jpg and NASA/Johns Hopkins APL/Steve Gribbe", ha="center", fontsize=12, bbox={"alpha":0.5, "pad":5})
plt.show()