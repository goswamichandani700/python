# write a program that return qube of given number 
def getqube(number):
    qube= number * number * number 
    return qube   


num = int(input("Enter number"))
#call getqube
answer = getqube(num)
print(answer)