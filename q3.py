#A3
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

rf = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")

#convert price and chg% to numeric
rf['Price'] = pd.to_numeric(rf['Price'], errors='coerce')
rf['Chg%'] = pd.to_numeric(rf['Chg%'])


rf = rf.dropna(subset=['Price', 'Chg%'])

mean= statistics.mean(rf['Price'])#for mean
variance= statistics.variance(rf['Price'])# for variance

print("Mean of Price:", mean)
print("Variance of Price:", variance)

wed_prices = rf[rf['Day'] == 'Wed']['Price']
mean_wed = statistics.mean(wed_prices)

#we are finding mean only for wednesday
print("Mean for wednesday:", mean_wed)
print("Population Mean:", mean)

#for april data we are finding mean prices
april_prices = rf[rf['Month'] == 'Apr']['Price']
if not april_prices.empty:
    mean_apr = statistics.mean(april_prices)
    print("Mean for April:", mean_apr)
    print("Population Mean:", mean)
else:
    print("No data for April.")

#calculating probability of a loss
loss_days = rf[rf['Chg%'] < 0]
prob_loss = len(loss_days) / len(rf)
print("Probability of making a loss:", round(prob_loss, 4))

#profit for wednesday
wed = rf[rf['Day'] == 'Wed']
profit_wed_days = wed[wed['Chg%'] > 0]
profit_wed = len(profit_wed_days) / len(wed)
print("Wednesday Profit:", round(profit_wed, 4))

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
rf['Day'] = pd.Categorical(rf['Day'], categories=days, ordered=True)
rf = rf.sort_values('Day')

plt.scatter(rf['Day'], rf['Chg%'], color='blue')
plt.xlabel('Day of the Week')
plt.ylabel('Chg%')
plt.title('Chg% vs Day of the Week')
plt.grid(True)
plt.show()
