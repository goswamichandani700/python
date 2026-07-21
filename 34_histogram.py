import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Read the CSV file
result = pd.read_csv('steve_smith.csv')

# Create Histogram chart with KDE curve
sns.histplot(data=result, x='score', kde=True, bins=10)

plt.title("Steve Smith ODI Career Scores Distribution")
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.grid(which='both')
plt.show()