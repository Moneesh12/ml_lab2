#A2

import pandas as pd

rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase data", usecols="A:E")
#we are going through the payment amount
for index, row in rf.iterrows():
    if row['Payment (Rs)'] > 200:#we are applying a condition to find if rich or poor
        print("RICH")
    else:
        print("POOR")
