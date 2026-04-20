 #write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 
# take input car
# input train 

average = int(input("enter average"))
km = int(input("enter km"))
petrol = int(input("enter petrol"))
train_price = int(input("enter price"))
car = (km/average) * petrol
print(car) 
if car>train_price:
    print("train price is cheaper")
if train_price>car:
    print("car is cheaper")







