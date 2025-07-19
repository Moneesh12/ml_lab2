#A6
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")

#replace t = 1 and f = 0
rf = rf.replace({'t': 1, 'f': 0}).infer_objects(copy=False)
rf = rf.replace('?', 0).infer_objects(copy=False)
rf = rf.apply(pd.to_numeric, errors='coerce').fillna(0)

v1 = rf.iloc[0].values
v2 = rf.iloc[1].values

#finding dot product and norm
dp = np.dot(v1,v2)
nA = np.linalg.norm(v1)
nB = np.linalg.norm(v2)
#for finding cosine similarity
cosAB = dp/(nA*nB)

print("the cosine similarity is",cosAB)