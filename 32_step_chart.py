# Create a step chart showing the percentage growth of Bitcoin and Ethereum.
import matplotlib.pyplot as plt

# 1. Timeline list: 12-Month tracking period
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# 2. Percentage Growth lists (Base 100% starting point)
bitcoin_growth = [
    100, 112, 108, 125, 140, 135, 
    148, 155, 150, 168, 185, 192
]

ethereum_growth = [
    100, 105, 115, 110, 132, 128, 
    142, 138, 145, 160, 172, 180
]

months = list(range(len(bitcoin_growth)))

plt.figure(figsize=(18,12))
plt.step(months,bitcoin_growth,where='mid',color='yellow')
plt.step(months,ethereum_growth,where='mid',color='grey')

plt.xlabel('weeks')
plt.xticks(ticks=months)
plt.ylabel('nifty and sensex')
plt.show()