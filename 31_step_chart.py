# Create a step chart showing changes in Nifty and Sensex over time.
import matplotlib.pyplot as plt

# 1. Timeline list: 12-week tracking period
weeks = [
    "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6",
    "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12"
]

# 2. Market Index lists (Simulated values matching respective point scales)
nifty_price = [
    22000, 22150, 21980, 22300, 22450, 22210,
    22500, 22760, 22620, 22900, 23100, 23050
]

sensex_price = [
    72400, 72900, 72350, 73400, 73850, 73100,
    74100, 74950, 74500, 75400, 76100, 75900
]

weeks = list(range(len(nifty_price)))

plt.figure(figsize=(18,12))
plt.step(weeks,nifty_price,where='mid',color='yellow')
plt.step(weeks,sensex_price,where='mid',color='grey')

plt.xlabel('weeks')
plt.xticks(ticks=weeks)
plt.ylabel('nifty and sensex')
plt.show()