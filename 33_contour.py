# Create a contour chart showing longitude, latitude, and internet signal strength.

import matplotlib.pyplot as plt 
import numpy as np

# 1. 1D arrays for Longitude and Latitude ranges
longitudes = np.linspace(-74.05, -73.90, 50)
latitudes = np.linspace(40.70, 40.85, 50)

# 2. Create a 2D grid from the 1D arrays
X, Y = np.meshgrid(longitudes, latitudes)

# print(X,Y)
internal_signal = -100 + 35 * np.exp(-((X - (-73.97))**2 + (Y - 40.78)**2) / 0.002)
print(X,Y,internal_signal)
plt.contour(X,Y,internal_signal,level=10,color='blue')
plt.show()