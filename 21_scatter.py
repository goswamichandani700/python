# Create a scatter chart displaying the score of RCB in each match since 2025.
import matplotlib.pyplot as plt
rcb_runs = [
    190, 106, 230, 189, 213, 203, 250, 201, 240, 149, 
    175, 206, 77, 155, 203, 167, 194, 222, 200, 254, 161
]
matches = list(range(1,len(rcb_runs)+1))

print(len(rcb_runs))

plt.figure(figsize=(18,12))
plt.scatter(rcb_runs,matches,s=25,c='blue',label='Sachin Runs in Odi')
plt.xlabel('rcb_runs')
plt.ylabel('matches')
plt.title('rcb match score 2025')
plt.show()