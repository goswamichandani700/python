
# Create a pie chart showing the smartphone market share of Realme, Redmi, Oppo, Vivo, Samsung, Apple, Nokia, and others.

import matplotlib.pyplot as plt

phones = ['realme','redmi','oppo','vivo','samsung','apple','nokia']

market_share = [21.0, 21.0, 12.0, 10.0, 4.0, 7.0, 1.0]

hex_colors = [
    "#A1C4FD",  
    "#E2E8F0",  
    "#96E6A1",  
    "#B0C4DE",  
    "#FF9999",  
    "#CBD5E1",  
    "#817F6F"]

plt.pie(market_share,labels=phones,colors=hex_colors,autopct='%1f%%')
plt.title('smartphone market share')
plt.show()