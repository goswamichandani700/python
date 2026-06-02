import matplotlib.pyplot as plt
import numpy as np
years = list(range(2000, 2026))

test_matches = [42, 45, 46, 41, 44, 46, 44, 34, 45, 33, 43, 38, 43, 42, 40, 43, 47, 45, 48, 39, 22, 45, 43, 41, 44, 42]

odi_matches = [142, 126, 153, 139, 122, 115, 148, 161, 118, 144, 147, 149, 107, 132, 128, 145, 112, 129, 121, 151, 44, 104, 141, 168, 118, 125]

t20_matches = [0, 0, 0, 0, 0, 1, 2, 23, 12, 51, 42, 29, 73, 56, 67, 64, 98, 64, 91, 310, 161, 319, 442, 504, 513, 480]
# create chart
plt.figure(figsize=(12, 6)) # Gives the chart a clean, wide look
plt.plot(years, test_matches, marker='s', linewidth=2, label='Test Matches')
plt.plot(years, odi_matches, marker='o', linewidth=2, label='ODI Matches')
plt.plot(years, t20_matches, marker='^', linewidth=2, label='T20 Matches')

# 2. Customize chart (Fixed string fonts to integers)
plt.title("All Format Matches Per Year", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Years", fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Matches', fontsize=11, fontweight='bold', labelpad=10)

plt.grid(which='both', linestyle='dotted', linewidth=0.7)

# 3. Fixed Legend placement and labels
plt.legend(loc='upper left', title='Match Formats')

# 4. Display chart configuration (Fixed limits to fit all data)
plt.xlim(left=1999, right=2026) 
plt.ylim(bottom=-20, top=560)  # Changed to completely cover a 0 to 513 match range safely

# 5. Fixed dynamic Y-ticks calc using a reliable 50-step interval up to 550
plt.yticks(np.arange(0, 561, 50))
plt.xticks(years, rotation=45)

plt.tight_layout()
plt.show()
