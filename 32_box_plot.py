import matplotlib.pyplot as plt 
import seaborn as sns 

# Load sample dataset
result = sns.load_dataset('titanic')

# Create Boxplot
sns.boxplot(data=result, x='class', y='age')
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.grid(which='both')
plt.show()