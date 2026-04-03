# write a program to count words  given string
name = input("what is your name")
print(name)
count = 1
for letter in name:
    if  letter == ' ':
        count = count + 1
print("no of words_count=",count)        




