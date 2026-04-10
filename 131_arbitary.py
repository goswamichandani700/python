#write a program to findout mean value from all the argument passed in function 
def find_mean(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
    

# Example usage
result = find_mean(10, 20, 30, 40, 50)
print("Mean value is:", result)