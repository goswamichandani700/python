import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Read CSV file
result = pd.read_csv('car_buyers.csv')

# Create KDE chart
sns.kdeplot(data=result, x='Age', fill=True)

plt.title("First-Time Car Buyers Age Distribution")
plt.xlabel('Age')
plt.ylabel('Density')
plt.grid(which='both')
plt.show()