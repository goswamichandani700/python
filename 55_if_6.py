#write a program to findout elder brother from given two brother's age. 
#input two brothers age

brother1 = int(input("enter age"))
brother2 = int(input("enter age"))
    
if brother1>0:
 print(f" age {brother1}")
if brother2>0:
    print(f"age{brother2}")

elder = brother2 - brother1
print(f"difference {elder}")


