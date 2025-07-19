#A1)

import pandas as pd
import numpy as np


rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase data", usecols="B:E", header=0)



A = rf.iloc[:,:-1].values

C = rf.iloc[:,-1].values.reshape(-1,1)

ATA = A.T.dot(A)#for transpose
ATC = A.T.dot(C)#for transpose

rankA = np.linalg.matrix_rank(A)#rank

A1 = np.linalg.pinv(A)#pseudo inverse



X = np.linalg.inv(ATA).dot(ATC)
print("A martix:\n",A)
print("C matrix:\n",C)
print("X matrix:\n",X)
print("dimension of A",A.shape)
print("dimension of C",C.shape)
print("rank of A",rankA)
print("pseudo inverse:",A1)
