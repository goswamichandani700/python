# Create a scatter chart showing Team India's total score in all T20I matches played so far.
import matplotlib.pyplot as plt 
# Team India T20I Innings Runs Only
runs = [
    127, 141, 218, 188, 157, 180, 186, 186, 159, 130, 
    146, 244, 260, 201, 209, 179, 151, 212, 160, 234, 
    212, 176, 297, 185, 168, 161, 209, 175, 255
]

print(len(runs))

plt.figure(figsize=(18,12))
matches = list(range(1,len(runs)+1))
plt.scatter(matches,runs,s=25,c='blue',label='Sachin Runs in Odi')
plt.xlabel('match')
plt.ylabel('runs')
plt.title('India t20i scores')
plt.show()