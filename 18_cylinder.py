#write a program to findout area & volume of cylinder.

radius = input('Enter radius')
height = input("Enter height")

radius = int(radius)
height = int(height)

area = 2 * 3.14 * radius * (height+radius)
volume = 3.14 * radius * radius * height
print("area",area)

print("volume",volume)



