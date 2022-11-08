
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('NEO Earth Close Approaches (2).csv')
df.head()
print(df)

print(df.dtypes)

df.plot(x = 'CA DistanceNominal (km)', y = 'Object')
plt.show