# write a program to display count of pass and failed failed (marks<35)
students = {
    "Aarav": 78, "Vihaan": 25, "Aditya": 92, "Arjun": 47, "Krishna": 83,
    "Ishaan": 56, "Rohan": 30, "Karan": 88, "Rahul": 74, "Amit": 61,
    "Neeraj": 95, "Suresh": 32, "Mahesh": 69, "Rajesh": 81, "Dinesh": 53,
    "Naresh": 37, "Mukesh": 11, "Anil": 44, "Sunil": 72, "Deepak": 85,
    "Vikas": 66, "Pankaj": 34, "Nitin": 90, "Gaurav": 58, "Manish": 76,
    "Tarun": 49, "Varun": 0, "Sanjay": 63, "Ajay": 97, "Vijay": 55
}
pass_count = 0
fail_count = 0



for marks in students:
    print(marks, students[marks])
    if students[marks]>35:
        pass_count = pass_count + 1
        
        
    else:
          fail_count = fail_count + 1
        
       
print("no of  pass count=",pass_count)
print("no of fail_count=",fail_count)
    

       




   


