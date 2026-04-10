#write a program to create function return simple Interest using keyword argument concept
def getsi(amount,rate,year):
    si = amount * rate * year/100
    return si


a = int(input("enter amount"))
r = float(input("enter rate"))
y = int(input("enter year"))
answer = getsi(amount=a,rate=r,year=y)

print(f"si={answer}")
