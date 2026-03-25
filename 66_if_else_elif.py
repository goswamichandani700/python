# write a program to accept 2 number from user. and accept choice for operations.
#operations will be addition, subtraction, multiplication, division
#do operation and display result.
''
#take  2 numbers of input.
# get addition
# do subtraction
# do multiplication
# do division
''
num1 = int(input("enter number"))
num2 = int(input("enter number"))
choice = int(input("enter your choice"))
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")

if choice == 1:
    addition = num1 + num2
    print(f"addition = {addition}")
elif choice == 2:
    subtraction = num1 - num2
    print(f"subtraction = {subtraction}")
elif choice == 3:
    multiplication = num1 * num2
    print(f"multiplication = {multiplication}")
else:
    division = num1 / num2
    print(f"division = {division}") 



          






 
       




