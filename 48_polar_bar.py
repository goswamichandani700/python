# Create a polar chart showing the number of runs scored by Virat Kohli in different field directions.

import matplotlib.pyplot as plt
import math

directions = ["Cover", "Point", "Mid-Wicket", "Square Leg",
              "Fine Leg", "Third Man", "Long-On", "Straight"]

degrees = [45, 90, 135, 180, 225, 270, 315, 0]

runs = [730, 650, 610, 560, 390, 420, 480, 520]

radians = [math.radians(deg) for deg in degrees]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

ax.plot(radians, runs, marker='o')
ax.fill(radians, runs, alpha=0.3)

for angle, run, direction in zip(radians, runs, directions):
    ax.text(angle, run + 30, direction, ha='center')

ax.set_title("Virat Kohli Runs by Field Direction")

plt.show()