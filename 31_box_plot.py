import matplotlib.pyplot as plt 
import seaborn as sns 

# Load sample dataset
result = sns.load_dataset('penguins')

# Create Boxplot
sns.boxplot(data=result, x='species', y='body_mass_g')
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.grid(which='both')
plt.show()