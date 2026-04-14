#write a program to generate qube of all the numbers in list using map function

numbers = [1,2,3,4,5]
cubes = map(lambda num: num * num * num,numbers)
print(list(cubes))