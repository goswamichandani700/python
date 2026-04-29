filename = input("Enter file name to create") #states.txt
mode = 'w' 

#file open
try:
   with open(filename,mode) as file:
      content = input("what do you want to save in file?")
      file.write(content) #this content will be return into file 
   print("file has been created successfully")
except PermissionError:
    print("you do not have permission to create this file")            
