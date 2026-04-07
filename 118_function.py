#write a program that return simple interest of given amount rate year 
def getsi(amount,rate,year):
    si = amount * rate * year/100
    return si


amount = int(input("enter amount"))
rate = float(input("enter rate"))
year = int(input("enter year"))
answer = getsi(amount,rate,year)

print("si=",answer)



