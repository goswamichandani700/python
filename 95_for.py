# write a program to display students who are failed (marks<35)
students = {
    "Aarav": 78, "Vihaan": 25, "Aditya": 92, "Arjun": 47, "Krishna": 83,
    "Ishaan": 56, "Rohan": 30, "Karan": 88, "Rahul": 74, "Amit": 61,
    "Neeraj": 95, "Suresh": 32, "Mahesh": 69, "Rajesh": 81, "Dinesh": 53,
    "Naresh": 37, "Mukesh": 11, "Anil": 44, "Sunil": 72, "Deepak": 85,
    "Vikas": 66, "Pankaj": 34, "Nitin": 90, "Gaurav": 58, "Manish": 76,
    "Tarun": 49, "Varun": 0, "Sanjay": 63, "Ajay": 97, "Vijay": 55
}
for marks in students:
    # print(marks, students[marks])
    if students[marks]<35:
        print(marks, "=", students[marks])
         
    
    
      