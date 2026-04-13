# write a program to findout minimum & maximum from all the argument passed in function and return it 
def getmin_max(*numbers):
    max_value = numbers[0]
    min_value = numbers[0]

    for index in range(1, len(numbers)):
        if numbers[index] > max_value:
            max_value = numbers[index]

        if numbers[index] < min_value:
            min_value = numbers[index]

    return max_value, min_value


result = getmin_max(85, 5, 125, 800, 99)
print("min and max:", result)
   