#  write a program to findout whether given year is leap year or not. 
# accept current year from user.
year = int(input("enter year"))
reminder1 = year % 4
reminder2 = year % 100
reminder3 = year % 400
if reminder1==0 and reminder2!=0:
   print("this year is leap year")
else:
   if reminder2==0 and reminder3!=0:
      print("this year is leap year ")
   else:
       print("this year is not leap year")
    
        


      



  
    
