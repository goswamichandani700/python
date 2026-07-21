import matplotlib.pyplot as plt 
import seaborn as sns 

# Load sample dataset
result = sns.load_dataset('diamonds')

# Create Boxplot
sns.boxplot(data=result, x='cut', y='price')
plt.xlabel("Cut Quality")
plt.ylabel("Price ($)")
plt.grid(which='both')
plt.show()