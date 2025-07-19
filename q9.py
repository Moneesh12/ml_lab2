#A9
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
rf = rf.replace({'t': 1, 'f': 0})
rf = rf.replace('?', pd.NA)

# filling the missing values with mode values
rf['sex'] = rf['sex'].fillna(rf['sex'].mode(dropna=True)[0])

# filling the missing values with mean values
rf['age'] = pd.to_numeric(rf['age'], errors='coerce')
rf['age'] = rf['age'].fillna(rf['age'].mean())

# filling the missing values with median values
rf['TSH'] = pd.to_numeric(rf['TSH'], errors='coerce')
rf['TSH'] = rf['TSH'].fillna(rf['TSH'].median())

scaler = MinMaxScaler()

#normalizing the attributes where necessary
normalize = ['age', 'TSH']

rf[normalize] = scaler.fit_transform(rf[normalize])

print(rf[['age', 'TSH']].head())
