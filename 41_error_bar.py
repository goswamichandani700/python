# Create an error bar chart showing the sales performance of 5 products over 30 days.
import matplotlib.pyplot as plt

# 1. Data formatted as Python lists
products = ['Product C', 'Product A', 'Product E', 'Product B', 'Product D']

# Average daily units sold over a 30-day period
average_sales = [150.2, 120.5, 110.8, 85.4, 60.1]  

# Day-to-day sales variance (Standard Deviation) over 30 days
errors = [10.5, 15.2, 30.1, 25.4, 8.3]


plt.errorbar(products,average_sales,errors,color='blue',capsize=10,fmt='o')
plt.title("teams performance in T20 along with errors")
plt.xlabel("teams")
plt.ylabel("average")
plt.grid()
plt.xticks(products,rotation=45)
plt.tight_layout()
plt.show()