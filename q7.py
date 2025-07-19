#A7
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")

rf =  rf.replace({'t':1,'f':0})
rf = rf.apply(pd.to_numeric, errors='coerce').fillna(0)


cols = [
    'on thyroxine', 'query on thyroxine', 'on antithyroid medication',
    'sick', 'pregnant', 'thyroid surgery', 'I131 treatment',
    'query hypothyroid', 'query hyperthyroid', 'lithium',
    'goitre', 'tumor', 'hypopituitary', 'psych',
    'TSH measured', 'T3 measured', 'TT4 measured', 'T4U measured',
    'FTI measured', 'TBG measured'
]

#first 20 rows selected
v1 = rf[cols].iloc[:20].to_numpy()
v2 = rf.iloc[:20].to_numpy()

#initialising matrices
cosine_matrix = np.zeros((20, 20))
jc_matrix = np.zeros((20, 20))
smc_matrix = np.zeros((20, 20))

#we are using this to find our Jacard, SMC and Cosine Similarity
for i in range(20):
    for j in range(20):
        vec1 = v1[i]
        vec2 = v1[j]

        f11 = 0
        f00 = 0
        f10 = 0
        f01 = 0


        for k in range(len(vec1)):

            if vec1[k]==1 and vec2[k]==1:
                f11 = f11 + 1
            elif vec1[k]==0 and vec2[k]==0:
                f00 = f00 + 1
            elif vec1[k]==0 and vec2[k]==1:
                f01 = f01 + 1
            elif vec1[k]==1 and vec2[k]==0:
                f10 = f10 + 1

        #these parts are for storing the JC, SMC, cosine similarity values

        JC = (f11) / (f01+ f10+ f11)if (f01 + f10 + f11) != 0 else 0

        SMC = (f11 + f00) / (f00 + f01 + f10 + f11) 
        jc_matrix[i][j] = JC
        smc_matrix[i][j] = SMC



        mat_vec1 = v1[i]
        mat_vec2 = v1[j]
        dp = np.dot(mat_vec1, mat_vec2)
        nA = np.linalg.norm(mat_vec1)
        nB = np.linalg.norm(mat_vec2)
        cosAB = 0 if nA == 0 or nB == 0 else dp / (nA * nB)
        cosine_matrix[i][j] = cosAB

plt.figure(figsize=(18, 5))

# Jaccard heatmap
plt.subplot(1, 3, 1)
sns.heatmap(jc_matrix, cmap='YlGnBu', annot=False)
plt.title('Jaccard Coefficient Heatmap')

# SMC heatmap
plt.subplot(1, 3, 2)
sns.heatmap(smc_matrix, cmap='YlOrRd', annot=False)
plt.title('Simple Matching Coefficient Heatmap')

# Cosine similarity heatmap
plt.subplot(1, 3, 3)
sns.heatmap(cosine_matrix, cmap='PuBuGn', annot=False)
plt.title('Cosine Similarity Heatmap')

plt.tight_layout()
plt.show()
