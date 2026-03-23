# write a program to accept length and width of two different farm from user. and findout & display which farm is bigger 
#input length and width
length1 = int(input("enter length"))
width1 = int(input("enter width"))

# == != < > <= >= 
area1 = length1 * width1
if area1>0:
    print(f"lenght1 and width1 {area1}")

length2 = int(input("enter length2 "))    
width2 = int(input("enter width2"))

area2 = length2 * width2
if area2>0:
    print(f"length2 and width2 {area2}")

area = area2>area1
print(area)   