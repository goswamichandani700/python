#create empty list cars
cars = [] #empty list
print(cars)

#add new cars
cars.append('maruti')
cars.append('mahindra')
cars.append('tata')
print(cars)

#insert new car
cars.insert(0, 'bmw')
print(cars)

cars.insert(1, 'mercedes')
print(cars)

scooters = ['passion','activa']
cars.extend(scooters)
print(cars)

#remove
cars.pop(0)
print(cars)

#empty
scooters.clear()
print(scooters)