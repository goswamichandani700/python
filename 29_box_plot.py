import matplotlib.pyplot as plt 
import seaborn as sns 

# Load sample dataset
result = sns.load_dataset('attention')

# Create Boxplot
sns.boxplot(data=result, x='attention', y='score')
plt.xlabel("Attention Level")
plt.ylabel("Score")
plt.grid(which='both')
plt.show()
