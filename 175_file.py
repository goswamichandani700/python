# write a program to count words in given file.
filename = input("Enter file name to read") 
mode = 'r' 

#file open
file = open(filename,mode) 
count = 0

#read text from file line by line 
for word in file:
    print(word.strip()) #remove new line character from both side of line
    count += 1
file.close()     
           
print("Total words:", count)