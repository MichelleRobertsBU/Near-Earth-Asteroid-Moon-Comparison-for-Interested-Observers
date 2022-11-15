
import colorsys
from xml.dom.minidom import DocumentType
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

#rotate x-axis tick labels
plt.xticks(rotation=45)
  
plt.show()

#Create 2 Diameter Columns
df2 = pd.read_csv("NEO Earth Close Approaches (2).csv")
df2[['Min Diameter','Max Diameter']] = df2["Diameter"].str.split("-", expand=True)

print("\n After adding two new columns : \n", df2)

#Compare Min Diameter to Moon Diameter
df3 = pd.read_csv("NEO Earth Diameter.csv")
df3.head()
print(df3.dtypes)



print('The diameter of the Near Earth Asteroid in comparison to the diameter of the Moon is')
print(df3['Min Diameter'].div(3474000)*100)
values = ['Moon', 3474000, 3474000]
length = len(df3)
df3.loc[length] = values

#Bar chart of diameter comparison
df3 = df3 = pd.read_csv("NEO Earth Diameter.csv")
plt.rcParams["figure.figsize"] = [14.00, 6.50]
plt.rcParams["figure.autolayout"] = True
df3.plot(y = "Min Diameter", x = "Object", kind='bar')
plt.show()


plt.pie(df3['Min Diameter'], labels = df3['Object'])
plt.show()