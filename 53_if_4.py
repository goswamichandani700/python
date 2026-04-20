#write a program to convert 24 hours time into 12 hours fomat time and display it with am pm message.



hours = int(input("Enter hours"))
if hours>12:
    hours = hours - 12 
    msg = ' PM'
else:
    msg = ' AM'
print(f" {hours} {msg}")


    

