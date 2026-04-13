 #write a program to convert decimal number into octal number using recursion 
def printdecimal_to_octal(number):
    if number > 0:
        reminder = number % 8
        number = number // 8 #48 
        printdecimal_to_octal(number)
        print(reminder,end='')

number = int(input("Enter number"))
print("Octal:", end=" ")
printdecimal_to_octal(number)

