#write a program to convert 24 hours time into 12 hours fomat time and display it with am pm message.


hours = int(input("enter hours"))

difference = hours - 12
#== != < > <= >= 
if difference>0:
    print(f"format time with {difference}pm")

difference = hours - 12
# == != < > <= >=
if difference>0:
    print(f"format time with {difference}am ")

difference = hours - 12
if difference>0:
    print(f"invald output{difference}")    


    

