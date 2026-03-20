#write a program to find out profit or loss amount from given products purchase salse price
#input :purchase price & sale price
#process : calculate difference between purchase and sale price
#output : prfit or loss message

purchase_price = int(input("enter purchase price"))
sales_price = int(input("enter sales price"))

difference = sales_price - purchase_price

#== != < > <= >= 
if difference>0:
    print(f"you have made profit {difference}")

if difference<0:
    print(f"you have made loss of {difference}")     

