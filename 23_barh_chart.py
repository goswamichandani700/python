# Create a bar chart showing the yearly gold price increase Rate from 2010 to 2025
import matplotlib.pyplot as plt
plt.figure(figsize=(18,12))
years = [
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 
    2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
]

gold_rate = [
    29.5, 10.1, 7.0, -28.3, -1.5, -10.4, 8.5, 
    13.1, -1.6, 18.3, 25.1, -3.6, -0.3, 13.1, 12.1, 17.6
]
colors = ['#2ecc71' if rate >= 0 else '#e74c3c' for rate in gold_rate]

plt.barh(years,gold_rate,color=colors,edgecolor='black',align='center')
plt.xlabel('years')
plt.ylabel('gold_rate')
plt.title('gold price of 2010 to 2025')
plt.show()