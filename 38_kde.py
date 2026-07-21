import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Read CSV file
result = pd.read_csv('divorce_years.csv')

# Create KDE chart
sns.kdeplot(data=result, x='Years_After_Marriage', fill=True)

plt.title("Distribution of Marriage Duration Before Divorce")
plt.xlabel('Years After Marriage')
plt.ylabel('Density')
plt.grid(which='both')
plt.show()