# Create a line chart to display the number of Test matches played each year in men's cricket from 2000 to 2025.
import matplotlib.pyplot as plt
import numpy as np
years = list(range(2000, 2026))
matches = [42, 45, 46, 41, 44, 46, 44, 34, 45, 33, 43, 38, 43, 42, 40, 43, 47, 45, 48, 39, 22, 45, 43, 41, 44, 42]

#create chart
plt.plot(years,matches)

#customize chart
plt.title("TEST MATCHES")
plt.xlabel("years",fontsize='11',fontweight='bold',labelpad=10)
plt.ylabel('matches',fontsize='11',fontweight='bold',labelpad=10)

plt.grid(which='both',linestyle='dotted',linewidth=0.7)
plt.legend(loc='upper left',title=['test matches (india)'])
#display chart
plt.xlim(left=1999,right=2026) #start and stop value for x 
plt.ylim(bottom=44,top=218)

plt.yticks(np.arange(0, max(matches)+26, 26))
plt.xticks(years,rotation=45)
plt.tight_layout()
plt.show()