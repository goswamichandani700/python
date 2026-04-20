#write a program to convert & display farenhit into calcius
#input
fahrenheit = input("Enter fahrenheit: ")
fahrenheit = float(fahrenheit)

# process (formula)
celsius = (fahrenheit - 32) / 1.8
celsius = round(celsius, 2)

print("Celsius =", celsius)
