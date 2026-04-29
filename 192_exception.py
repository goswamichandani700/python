filename = input("Enter file name to read") #states.txt
mode = 'r' 

#file open
try:
      with open(filename,mode) as file:
      #read text from file line by line 
         for line in file:
            print(line.strip())
except FileNotFoundError:
    print("file not found.enter correct file name.")            

          















