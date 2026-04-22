# write a program to display given file content in reverse on screen. 
#     steps 1) create list 
#           2) open file 
#           3) read content from file and append in list 
#           4) after all content read, display list in reverse 

filename = input("Enter file name to create") 
mode = 'r' 
lines = []
#file open
with open(filename,mode) as file:
   for line in file:
      lines.append(line.strip())
   
lines.reverse()
for line in lines:
    print(line)

    
    












