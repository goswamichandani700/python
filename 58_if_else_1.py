# write a program to findout & display given shape is portrait or landscape using decision making statement if else 
'''
step 
    accept length from user 
    accept width from user 
    if length>width
      print shape is portrait
    else 
      print shap is landscape 
'''

length = int(input("enter length"))
width = int(input("enter width"))

if length>width:
    print("shape of portrait")
else:
    print("shape of landscape")    
