# Create a line chart to display the number of ODI matches played each year in men's cricket from 2000 to 2025.
import matplotlib.pyplot as plt
import numpy as np 
years = list(range(2000, 2026))
matches = [148, 122, 158, 172, 131, 114, 168, 186, 124, 161, 150, 146, 112, 156, 126, 152, 107, 131, 130, 154, 44, 73, 164, 218, 112, 118]

#create chart
plt.plot(years,matches)

#customize chart
plt.title("ODI MATCHES")
plt.xlabel("years",fontsize='11',fontweight='bold',labelpad=10)
plt.ylabel('matches',fontsize='11',fontweight='bold',labelpad=10)

plt.grid(which='both',linestyle='dotted',linewidth=0.7)
plt.legend(loc='upper left',title=['odi matches (india)'])
#display chart
plt.xlim(left=1999,right=2026) #start and stop value for x 
plt.ylim(bottom=44,top=218)

plt.yticks(np.arange(0, max(matches)+26, 26))
plt.xticks(years,rotation=45)
plt.tight_layout()
plt.show()