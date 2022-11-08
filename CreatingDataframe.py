import pandas as pd

#read with headers
df=pd.read_csv("NEO Earth Close Approaches (2).csv", nrows=10)

#display
print(df)

df=pd.read_csv("NEO Earth Close Approaches (2).csv")

# Get the total number of rows
rowCount = df.shape[0]
print('Total rows are ')
print(rowCount)

# Get the total number of columns
columnCount = df.shape[1]
print('Total columns are ')
print(columnCount)