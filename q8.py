#A8
import pandas as pd

rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="thyroid0387_UCI")
rf = rf.replace({'t': 1, 'f': 0})
rf = rf.replace('?', pd.NA)

print(rf.isnull().sum())

# filling the missing values with mode values
rf['sex'] = rf['sex'].fillna(rf['sex'].mode(dropna=True)[0])

# filling the missing values with mean values
rf['age'] = pd.to_numeric(rf['age'], errors='coerce')
rf['age'] = rf['age'].fillna(rf['age'].mean())

# filling the missing values with median values
rf['TSH'] = pd.to_numeric(rf['TSH'], errors='coerce')
rf['TSH'] = rf['TSH'].fillna(rf['TSH'].median())

print(rf.head(10))
