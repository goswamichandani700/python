# Create an error bar chart showing the scores of all IPL teams in the 2026 season.
import numpy as np
import matplotlib.pyplot as plt

teams = [
    'Sunrisers Hyderabad', 
    'Royal Challengers Bengaluru', 
    'Gujarat Titans', 
    'Rajasthan Royals', 
    'Punjab Kings', 
    'Kolkata Knight Riders', 
    'Delhi Capitals', 
    'Chennai Super Kings', 
    'Mumbai Indians', 
    'Lucknow Super Giants'
]

# Average runs scored per match in the 2026 season
average = [198.40, 191.50, 186.20, 184.80, 181.20, 179.00, 178.50, 176.40, 174.20, 172.80]

# Score variance / match-to-match fluctuation margin
errors = [31.80, 24.50, 21.20, 22.10, 19.50, 25.40, 23.00, 18.90, 20.60, 21.40]

plt.errorbar(teams,average,errors,color='blue',capsize=10,fmt='o')
plt.title("teams performance in T20 along with errors")
plt.xlabel("teams")
plt.ylabel("average")
plt.grid()
plt.xticks(teams,rotation=45)
plt.tight_layout()
plt.show()