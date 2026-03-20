#write a program to reverse 3 digit amount given by user.
#input : number 256 output 652 

amount = 256
amount = int(input("enter number"))
print(amount)

last = amount % 10 # 6
print(last)

remaining = amount // 10 #25
print(remaining)

middle = remaining % 10 #5
print(middle)

first = remaining // 10 #2
print(first)

amount =( last * 100 + middle * 10 + first)
print(amount)