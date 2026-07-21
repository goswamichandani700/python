import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

# Read the CSV file
result = pd.read_csv('ipl_team_scores.csv')
print(result)

# Create strip plot chart
sns.stripplot(data=result, x='Team', y='Score', jitter=True)

plt.title("Strip Plot Chart of IPL Team Scores (Since 2008)")
plt.xlabel("Team")
plt.ylabel("Runs Scored")
plt.grid(which='both')
plt.show()