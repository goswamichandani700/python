#BoxPlot chart 
#Create a BoxPlot chart that display marks of 4 different division of school. each division is list that has marks of 50 students. 
   #  A division marks range 40 to 50
   #  B division marks range 51 to 65
   #  C division marks range 66 to 80
   #  D division marks range 81 to 90

import matplotlib.pyplot as plt 

Division_A = [
    46, 43, 50, 47, 44, 46, 49, 42, 46, 50, 43, 40, 50, 41, 44, 41, 41, 40, 49, 44, 
    41, 43, 49, 48, 48, 50, 41, 43, 48, 45, 43, 40, 44, 47, 43, 50, 46, 50, 44, 47, 
    49, 49, 42, 45, 41, 46, 43, 40, 43, 45
]

Division_B = [
    63, 51, 64, 52, 60, 56, 54, 57, 56, 51, 57, 52, 63, 62, 53, 58, 62, 59, 65, 59, 
    55, 60, 53, 62, 55, 61, 54, 59, 61, 64, 60, 60, 60, 65, 54, 63, 56, 58, 51, 58, 
    57, 57, 55, 55, 65, 55, 53, 52, 59, 60
]

Division_C = [
    68, 73, 77, 68, 73, 77, 69, 74, 75, 66, 75, 72, 79, 74, 80, 72, 79, 74, 80, 68, 
    73, 77, 67, 73, 74, 75, 66, 75, 66, 79, 73, 67, 73, 77, 69, 74, 75, 66, 75, 72, 
    79, 74, 80, 72, 79, 74, 80, 68, 73, 77
]

Division_D = [
    81, 86, 82, 83, 83, 86, 81, 87, 83, 83, 82, 83, 83, 86, 84, 85, 86, 89, 84, 81, 
    86, 82, 83, 83, 86, 81, 87, 83, 83, 82, 83, 83, 86, 84, 85, 86, 89, 84, 81, 86, 
    82, 83, 83, 86, 81, 87, 83, 83, 82, 90
]

list = [Division_A,Division_B,Division_C,Division_D]

plt.boxplot(list,labels=['Division_A','Division_B','Division_C','Division_D'])

plt.xlabel("Divisions")
plt.ylabel("Student Marks")
plt.title("Comparison of Student Performance by Division")
plt.show()
