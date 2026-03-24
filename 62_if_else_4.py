# write a program to findout which triangle is bigger in area from given 2 triangle base and length 
base1 = int(input("enter base1"))
length1 = int(input("enter legth1")) 
area1 =   base1 * length1
print(area1)

base2 = int(input("enter base2"))
length2 = int(input("enter length2"))
area2 = base2 * length2
print(area2)
if area1>area2:
    print("first triangle is big")
else:
    print("second triangle is bigger")    
   

