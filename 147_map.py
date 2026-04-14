#write a program to convert all the negative numbers into positive number in list using map function 
numbers = [5, -3, 7, -1, -9, 4]
positive_numbers = (map(lambda num: -num if num<0 else num,numbers)) 
print(list(positive_numbers))