# Create a contourf chart showing sugar quantity (grams), tea boiling time (minutes), and user ratings.
import matplotlib.pyplot as plt
import numpy as np

# 1. 1D arrays for Sugar Quantity (0 to 20 grams) and Boiling Time (2 to 10 minutes)
sugar_qty = np.linspace(0, 20, 100)
boiling_time = np.linspace(2, 10, 100)

# 2. Create a 2D grid from the 1D arrays
X, Y = np.meshgrid(sugar_qty, boiling_time)

# 3. Simulate User Ratings (Scale of 1 to 5 stars)
# Creating a sweet spot for perfect tea: 8 grams of sugar and 6 minutes of boiling time
user_ratings = 1 + 4 * np.exp(-((X - 8.0)**2 / 30 + (Y - 6.0)**2 / 8))

# 4. Initialize the plot layout
fig, ax = plt.subplots(figsize=(10, 6))

# 5. Generate the filled contour plot (contourf)
# Using 'RdYlGn' (Red-Yellow-Green) colormap so higher ratings look green
filled_contour = ax.contourf(X, Y, user_ratings, levels=15, cmap='RdYlGn')

# 6. Add a colorbar to act as a legend for the ratings
colorbar = fig.colorbar(filled_contour, ax=ax)
colorbar.set_label('User Ratings (1 to 5 Stars)', fontweight='bold', labelpad=10)

# Formatting labels, titles, and grid lines
ax.set_xlabel('Sugar Quantity (Grams)', fontweight='bold', labelpad=10)
ax.set_ylabel('Tea Boiling Time (Minutes)', fontweight='bold', labelpad=10)
ax.set_title('Tea Preference Analysis: Impact of Sugar & Boiling Time on Ratings', fontweight='bold', fontsize=14, pad=15)

# Adjust plot boundaries cleanly
fig.tight_layout()
plt.show()

# Save the generated visualization 
plt.savefig('tea_rating_contourf.png', dpi=300)
