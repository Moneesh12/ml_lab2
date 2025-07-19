#A4
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")

rf.info() # Display data types and non-null counts

rf.describe(include = 'all')

#this function is for classification of binary, categorical and numerical
def datatype(cols):
    n = cols.nunique()
    if cols.dtype == 'object':
        if n == 2:
            return 'Binary'
        elif 2<n<10:
            return 'Categorical'
        else:
            return 'Numeric'

for cols in rf.columns:
    print(f"{cols}: {datatype(rf[cols])}")


lt = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI",
                   usecols=['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI', 'TBG'])
for col in lt.columns:
    lt[col] = pd.to_numeric(lt[col], errors='coerce')

print("data range min,max",lt.agg(['min','max']))

print("missing values",lt.isnull())

#for finding outlier
lt.boxplot(figsize=(10, 4))
plt.title("Outlier Detection using Boxplot")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
