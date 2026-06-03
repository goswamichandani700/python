# Create a scatter chart displaying the age of patient at the time of death in covid 19.
import matplotlib.pyplot as plt

patient_death = [
    34, 80, 73, 80, 63, 14, 74, 78, 69, 70, 56, 62, 90, 90, 72, 82, 84, 39, 70, 89, 
    74, 73, 76, 53, 69, 69, 55, 75, 47, 63, 76, 69, 86, 76, 74, 79, 62, 75, 39, 66, 
    72, 79, 74, 80, 84, 68, 82, 83, 83, 33, 68, 81, 77, 67, 73, 48, 86, 74, 75, 66, 
    59, 75, 48, 59, 76, 51, 58, 66, 79, 73, 81, 63, 63, 92, 79, 68, 73, 77, 64, 78
]
patient_index = list(range(1, len(patient_death) + 1))
print(len(patient_death))

plt.figure(figsize=(18,12))
matches = list(range(1,len(patient_death)+1))
plt.scatter(patient_death,patient_index,s=25,c='blue',label='Sachin Runs in Odi')
plt.xlabel('Patient Case Index (1-80)')
plt.ylabel('Age at Time of Death (Years)')
plt.title('Age of Patients at Time of Death in COVID-19')
plt.show()