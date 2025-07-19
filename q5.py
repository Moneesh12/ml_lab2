#A5
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")

#columns to convert t/f to 1/0
cols = [
    'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
    'sick', 'pregnant', 'thyroid surgery', 'I131 treatment',
    'query hypothyroid', 'query hyperthyroid', 'lithium',
    'goitre', 'tumor', 'hypopituitary', 'psych',
    'TSH measured', 'T3 measured', 'TT4 measured', 'T4U measured',
    'FTI measured', 'TBG measured'
]

for i in cols:
    rf [i] = rf[i].replace({'t':1,'f':0})

v1 = rf.iloc[0][cols].values
v2 = rf.iloc[1][cols].values

#initialise to all 0
f11 = 0
f00 = 0
f10 = 0
f01 = 0

# Compare elements to compute pairwise counts
for i in range(len(v1)):
    if v1[i]==1 and v2[i]==1:
        f11 = f11 + 1
    elif v1[i]==0 and v2[i]==0:
        f00 = f00 + 1
    elif v1[i]==0 and v2[i]==1:
        f01 = f01 + 1
    elif v1[i]==1 and v2[i]==0:
        f10 = f10 + 1

#formula
JC = (f11) / (f01+ f10+ f11)
SMC = (f11 + f00) / (f00 + f01 + f10 + f11) 


print("jacard",JC)
print("Simple Matching Coefficient",SMC)