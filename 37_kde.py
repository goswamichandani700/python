import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Read CSV file
result = pd.read_csv('marriage_age_india.csv')

# Create KDE chart
sns.kdeplot(data=result, x='Age', fill=True)

plt.title("First-Time Marriage Age Distribution in India")
plt.xlabel('Age (Years)')
plt.ylabel('Density')
plt.grid(which='both')
plt.show()