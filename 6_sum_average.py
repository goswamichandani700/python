#write a program to make sum & average of 3 user given 3 subject marks (english,maths,science) and display it

english = input("Enter english")
maths = input("Enter maths")
science = input("Enter science")

english = int(english)
maths = int(maths)
science = int(science)

sum = english + maths + science
print("subject marks of english,maths,science=",sum)

average = sum/3
print("subject marks of english,maths,science=",average)