
# write a program to convert 24 hours time into 12 hours format time and display it with AM PM   message. 


hours = int(input("enter hours"))

difference = hours - 12
#== != < > <= >= 
if difference>0:
    print(f"format time with {difference}pm")
else:
    print(f"format time with {difference} am")
