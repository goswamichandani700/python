# Create a line chart to display the number of T20 matches played each year in men's cricket from 2000 to 2025.
import matplotlib.pyplot as plt
import numpy as np
years = list(range(2000, 2026))
t20_matches = [0, 0, 0, 0, 0, 1, 2, 23, 12, 51, 42, 29, 73, 56, 67, 64, 98, 64, 91, 310, 161, 319, 442, 504, 513, 480]
# create chart
plt.plot(years,t20_matches)

#customize chart
plt.title("T20 MATCHES")
plt.xlabel("years",fontsize='11',fontweight='bold',labelpad=10)
plt.ylabel('matches',fontsize='11',fontweight='bold',labelpad=10)

plt.grid(which='both',linestyle='dotted',linewidth=0.7)
plt.legend(loc='upper left',title=['test matches (india)'])
#display chart
plt.xlim(left=1999,right=2026) #start and stop value for x 
plt.ylim(bottom=44,top=218)

plt.yticks(np.arange(0, max(t20_matches)+26, 26))
plt.xticks(years,rotation=45)
plt.tight_layout()
plt.show()