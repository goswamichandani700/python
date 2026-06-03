# Create a bar chart showing the annual Sensex return from 2010 to 2025.
import matplotlib.pyplot as plt

years = [
    "2010", "2011", "2012", "2013", "2014", "2015", "2016", 
    "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"
]

sensex_returns = [
    17.4, -24.6, 25.7, 9.0, 29.9, -5.0, 2.0, 
    27.9, 5.9, 14.4, 15.8, 22.0, 4.4, 18.7, 13.8, 11.2
]

bar_colors = [ "#3A225D",
           "#00B7F1"  ]

plt.barh(years,sensex_returns,color=bar_colors,edgecolor='black',align='center')
plt.xlabel('years')
plt.ylabel('sensex return')
plt.title('annual sensex return 2010 to 2025')
plt.show()