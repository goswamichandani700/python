# write a program to accept length and width of two different farm from user. and findout & display which farm is bigger 
#input length and width
length1 = int(input("enter length1"))
width1 = int(input("enter width1"))
length2 = int(input("enter length2 "))    
width2 = int(input("enter width2"))
# == != < > <= >= 
area1 = length1 * width1
area2 = length2 * width2
if area1>area2:
    print("area1 is bigger")
if area2>area1:
    print("area2 is bigger")





