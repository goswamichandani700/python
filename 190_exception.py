filename = input("Enter file name to read") #states.txt
mode = 'r' 

#file open


#read text from file line by line
try: 
   with open(filename,mode) as file: 
      for line in file:
         print(line.strip()) #remove new line character from both side of line
except FileNotFoundError:
   print("file not found.please enter correct file name.")
# except Exception as e:
#    print("Error:",e)
