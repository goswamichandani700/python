# Create a dashboard containing 4 different chart types on a single screen. All charts should represent different aspects of the same topic. For example:

#  Line Chart: Monthly sales trend
#  Bar Chart: Product-wise sales
#  Pie Chart: Market share by product
#  Scatter Chart: Sales vs Profit analysis

import matplotlib.pyplot as plt 
import numpy as np 

# --- DATA SETS (Retail Business Performance) ---
months = np.arange(1, 13)
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# 1. Monthly Sales Trend (Line Chart)
monthly_sales = [45, 52, 49, 62, 58, 75, 82, 79, 88, 94, 110, 135] # in Thousands ($)

# 2. Product-wise Sales Volume (Bar Chart)
products = ['Laptops', 'Smartphones', 'Tablets', 'Headphones', 'Smartwatches']
product_sales = [120, 185, 95, 240, 150] # Units sold

# 3. Market Share by Product Category (Pie Chart)
market_share = [35, 28, 15, 12, 10] # Percentages

# 4. Sales vs Profit Analysis (Scatter Chart)
sales_volume = [15, 25, 38, 42, 55, 68, 80, 95, 110, 130] # In Thousands ($)
profit_earned = [2, 5, 4, 9, 11, 12, 18, 22, 20, 29] # In Thousands ($)
branches = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10']

plt.subplot(2, 2, 1)
plt.plot(months, monthly_sales, marker='o', color='blue', label='Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales (in $1K)')
plt.xticks(months, month_labels)
plt.yticks(np.arange(30, max(monthly_sales) + 20, 15))
plt.title('Monthly Sales Performance Trend')
plt.legend(loc='upper left')
plt.grid(which='both', linestyle='--', linewidth=0.5)

plt.subplot(2, 2, 2)
bars = plt.bar(products, product_sales, color='cyan', label='Units Sold', edgecolor='black', width=0.7)
for bar in bars:
    bar.set_hatch('//')  # Adds the custom diagonal line pattern

plt.xlabel('Product Categories')
plt.ylabel('Units Sold')
plt.yticks(np.arange(0, max(product_sales) + 30, 30))
plt.title('Product-wise Total Volume Sales')
plt.legend(loc='upper right')
plt.grid(which='both', linestyle='--', linewidth=0.5)

plt.subplot(2, 2, 3)
hex_colors = [
    "#A1C4FD",  
    "#E2E8F0",  
    "#96E6A1",  
    "#B0C4DE",  
    "#FF9999",  
    "#CBD5E1",  
    "#817F6F"]

plt.pie(market_share,labels=market_share,colors=hex_colors,autopct='%1f%%')
plt.title('smartphone market share')

plt.subplot(2, 2, 4)
# REMOVED: plt.figure(figsize=(18,12)) -> This was destroying your 4-chart layout!

plt.scatter(sales_volume, profit_earned, s=50, c='blue', label='sales and profit', edgecolors='black')
plt.xlabel('sales')
plt.ylabel('profit')
plt.title('sales vs profit')
plt.legend(loc='upper left')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.show()