# write a program to print 30 to 21 multiplication table 
# 30 x 1 = 30
# 30 x 2 = 60
# 30 x 10 = 300
number = 30
while number>=21:
    multiplier = 1
    while multiplier<=10:
        result = number * multiplier
        print(f"{number} X {multiplier} = {result}")
        multiplier = multiplier + 1
    number = number - 1
