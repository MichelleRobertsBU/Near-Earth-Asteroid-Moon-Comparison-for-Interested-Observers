
import colorsys
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