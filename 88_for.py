# display only values divisible by 10 from tuples (use operator %)
numbers = (12, 45, 78, 23, 56, 91, 34, 67, 89, 10, 54, 32, 76, 88, 21, 43, 65, 99, 27, 58)
count = 0
for item in numbers:
    #print(item, end=' ')
    reminder = item % 10
    if reminder == 0:
        print(item, end=' ')
print("numbers of divisible values=",numbers)        
       



