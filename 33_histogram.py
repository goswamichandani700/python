import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Read CSV file
result = pd.read_csv('virat_kohli.csv')

# Create Histogram chart with KDE overlay
sns.histplot(data=result, x='score', kde=True, bins=10)

plt.title("Virat Kohli ODI Career Scores Distribution")
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.grid(which='both')
plt.show()