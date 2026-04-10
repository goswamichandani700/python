#write a program to findout minimum value from all the argument passed in function
def getSum(*numbers):
    # here numbers is tuple
    min = numbers[0]
    for index in range(1,len(numbers)):
         if numbers[index]<min:
              min = numbers[index]
    return min            
min = getSum(85,5,125,800,99)
print(min)