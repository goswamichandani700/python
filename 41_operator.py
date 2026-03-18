#operators
#write a program to convert given grams into kilograms and remaining grams.

grams = int(input('enter grams'))

kilograms = grams // 1000
kilograms = kilograms % 1000

print('grams=',grams ,'kilograms=',kilograms)