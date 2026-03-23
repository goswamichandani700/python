 #write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 
# take input car
# input train 

car = int(input("enter price"))
train = int(input("enter price"))
travel = car - train
print(f"cheaper {travel}")

if car>0:
    print(f"price of {car}")

if train>0:
    print(f"price of{train}") 




