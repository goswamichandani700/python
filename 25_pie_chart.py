# Create a pie chart showing the percentage of students in Gujarat who opted for Commerce, Arts, Science, and Diploma after the 10th standard.

import matplotlib.pyplot as plt

courses = ['commerce', 'arts', 'science','diploma']

students = [52.0, 24.5, 16.5, 7.0]

bar_colors = ["#FF9999","#A7F3D0","#A1C4FD","#817F6F"]

plt.pie(students,labels=courses,colors=bar_colors,autopct='%1f%%')
plt.title('students of different courses')
plt.show()
