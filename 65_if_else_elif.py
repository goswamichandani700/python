#Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

#| Percentage | Grade |

# 90–100     | A+    |
 #80–89      | A     |
 #70–79      | B     |
 #60–69      | C     |
 #50–59      | D     |
 #below 50   | Need to improve  |
''''''
#takes input 5 subject marks
# get total
# get percentage
# display grade
''
maths = int(input("enter marks"))
science = int(input("enter marks"))
english = int(input("enter marks"))
hindi = int(input("enter marks"))
computer = int(input("enter marks"))

sum = maths + science + english + hindi + computer
print(sum)

average = sum / 5
if average<50:
    print("need to improve")
elif average<59:
    print("grade {D}")
elif average<69:
    print("grade{C}") 
elif average<79:
    print("grade {B}")
elif average<89:
    print("grade {A}")
else:
    print("grade {A+}")







              