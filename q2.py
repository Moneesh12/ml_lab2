#A2

import pandas as pd

rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="Purchase data", usecols="A:E")

for index, row in rf.iterrows():
    if row['Payment (Rs)'] > 200:#we
        print("RICH")
    else:
        print("POOR")
